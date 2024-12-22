"""
implement function related to Markup Language Options
"""

MLO2PARSR_NAME = {
        'rst': 'reStructuredText',
        'md': 'myst'}

EXTENSION2PARSER_NAME = {
        'rst': 'reStructuredText',
        'md': 'myst'}


import re
import logging
import errno
import os


from .cli_utils import PROGRAM_NAME


global logger
logger = logging.getLogger(PROGRAM_NAME)


class MarkupLanguageOptionConfiguration(dict):

    def __new__(cls, *, rst_arg=None, md_arg=None,
                use_regex=None):
        return super().__new__(cls)

    def __init__(self, *, rst_arg=None, md_arg=None,
                use_regex=None):
        super().__init__({'rst': rst_arg, 'md': md_arg})
        self.use_regex = use_regex

    def initialize(self, is_single_or_web_server_mode):
        self.is_single_or_web_server_mode = is_single_or_web_server_mode

        self._initialize_clean_up_none()

        if is_single_or_web_server_mode:
            self._initialize_test_single_mode_or_web_server_mode()
        else: # recursive mode
            self._initialize_test_filter_legality()

    def _initialize_clean_up_none(self):
        # remove entries which value is None
        # i.e. this specific MLO is absent
        for key, value in self.copy().items():
            if value is None:
                self.pop(key)

    def _initialize_test_single_mode_or_web_server_mode(self):
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

    def _initialize_test_filter_legality(self):
        # test legality for each filter
        for language, filters in self.items():
            for fil in filters: # test for each pattern is legal

                # test regex pattern legality
                if self.use_regex:
                    try:
                        re.compile(fil)
                    except re.error:
                        logger.critical(
        'option --{} gets an illegal regex pattern: {}'.format(
                                language, repr(fil)))
                        exit(errno.EINVAL)

                # test extension legality
                else:
                    if not (fil and fil.isalnum()):
                        logger.critical(
        'option --{} gets an illegal extension: {}'.format(
                                language, repr(fil)))
                        exit(errno.EINVAL)

    def get_parser_name(self, src_file_path, src_info_path):
        if self:  # none empty
            mlo = list(self.keys())[0]
            return MLO2PARSR_NAME[mlo]

        else:  # auto determine by file extension
            _, extension = os.path.splitext(src_file_path)
            extension_nor = extension.lower()[1:]

            try:
                return EXTENSION2PARSER_NAME[extension_nor]
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
