"""
implement function related to Markup Language Options
"""

MLO2PARSR_NAME = {
        'rst': 'reStructuredText',
        'md': 'myst'}

EXTENSION2MLO = {
        'rst': 'rst',
        'md': 'md'}


import re
import logging
import errno
import os

from .cli_utils import PROGRAM_NAME


global logger
logger = logging.getLogger(PROGRAM_NAME)


class _MLOConfigSBase(dict):

    def __new__(cls, *, rst_arg=None, md_arg=None):
        return super().__new__(cls)

    def __init__(self, *, rst_arg=None, md_arg=None):
        super().__init__({'rst': rst_arg, 'md': md_arg})

    def _init_clean_up_none(self):
        """
        remove entries which value is ``None``; i.e. this specific MLO is absent
        """
        for key, value in self.copy().items():
            if value is None:
                self.pop(key)


class MLOConfigSingleWebServerMode(_MLOConfigSBase):

    def __init__(self, *, rst_arg=None, md_arg=None):
        super().__init__(rst_arg=rst_arg, md_arg=md_arg)
        self._init_clean_up_none()
        self._init_test_content()

    def _init_test_content(self):
        if len(self) > 1:
            logger.critical(
    "more than 1 markup langauge option is given in single/web server mode")
            exit(errno.EINVAL)

        if len(self) > 0:
            filters = list(self.values())[0]
            if filters:
                logger.critical(
        "single/web server mode not allow any FILTER: {}".format(
                        ', '.join(filters)))
                exit(errno.EINVAL)

    def get_language_parser_name(self, src_file_path, src_info_path):
        if self:  # none empty
            mlo = list(self.keys())[0]

        else:  # auto determine by file extension
            _, extension = os.path.splitext(src_file_path)
            extension_nor = extension.lower()[1:]

            try:
                mlo = EXTENSION2MLO[extension_nor]
            except KeyError:
                # generate error message
                msg_list = []
                msg_list.append(
        'can not automatically decide markup language from extension')
                if extension:
                    msg_list.append(extension)
                msg_list.append('of file:')
                msg_list.append(src_info_path)

                logger.critical(' '.join(msg_list))
                exit(errno.EINVAL)

        parser_name = MLO2PARSR_NAME[mlo]
        return mlo, parser_name


class MLOConfigRecursiveMode(_MLOConfigSBase):

    DEFAULT = {'rst': ['rst'], 'md': ['md']}

    def __new__(cls, *, rst_arg=None, md_arg=None, use_regex=None):
        return super().__new__(cls, rst_arg=rst_arg, md_arg=md_arg)

    def __init__(self, *, rst_arg=None, md_arg=None, use_regex=None):
        super().__init__(rst_arg=rst_arg, md_arg=md_arg)

        if all(v is None for v in self.values()):
            # none of MLO is present
            for language, extensions in self.DEFAULT.items():
                self[language] = extensions
            self.use_regex = False

        else:  # at least one of mlo is given
            self.use_regex = use_regex

            self._init_clean_up_none()
            self._init_test_at_least_one_filter()

            # test legalities of filters
            if self.use_regex:
                self._init_test_regex_legality()
            else:
                self._init_test_extension_legality()

    def _init_test_at_least_one_filter(self):
        """
        in recursive mode, at least 1 filter must be present per MLO
        """
        for language, filters in self.items():
            if len(filters) == 0:
                logger.critical(
        'option --{} must have at least one filter'.format(language))
                exit(errno.EINVAL)

    def _init_test_regex_legality(self):
        for language, regex_patterns in self.items():
            for pattern in regex_patterns:  # test for each filter regex
                try:
                    re.compile(pattern)
                except re.error:
                    logger.critical(
    'option --{} gets an illegal regex pattern: {}'.format(
                            language, repr(pattern)))
                    exit(errno.EINVAL)

    def _init_test_extension_legality(self):
        for language, extensions in self.copy().items():
            for idx, ext in enumerate(extensions):
                # test for each filter extension
                if not re.fullmatch(r'[0-9a-zA-Z]+', ext):
                    logger.critical(
                            'option --{} gets an illegal extension: {}'
                            .format(language, repr(ext)))
                    exit(errno.EINVAL)

                if re.search(r'[A-Z]', ext):  # contains upper case
                    new_ext = ext.lower()
                    msg = \
            'option --{} gets extension with upper case: {}, converted to {}' \
                            .format(language, repr(ext), repr(new_ext))
                    logger.warning(msg)
                    self[language][idx] = new_ext

    def select_and_get_language_parser_name(self, filename):
        """
        :param filename:
        :type filename: str
        :return: (language, parser_name) if selected; None if file not selected
        :rtype: tuple or NoneType
        """
        mlo = self._select_mlo_by_regex(filename) if self.use_regex \
                else self._select_mlo_by_extension(filename)

        if mlo is None:
            return None
        else:
            return mlo, MLO2PARSR_NAME[mlo]

    def _select_mlo_by_regex(self, filename):
        for language, regex_patterns in self.items():
            for pattern in regex_patterns:
                if re.fullmatch(pattern, filename):
                    return language

        return None

    def _select_mlo_by_extension(self, filename):
        _, file_ext = os.path.splitext(filename)
        file_ext = file_ext[1:]

        for language, extensions in self.items():
            for ext in extensions:
                if file_ext.lower() == ext:
                    return language

        return None
