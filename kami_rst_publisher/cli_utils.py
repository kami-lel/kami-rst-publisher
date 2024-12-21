"""
common utility functions used in CLI
"""


PROGRAM_NAME = 'kami_rst_publisher'
PRESETS = ['dark', 'light']  # used in options -p choices  # FIXME make as var
# stylesheets in STYLESHEET_DIR
PRESETS_STYLESHEET_PATHS = {
    'dark': ['responsive.css', "kami_html5.css",
            "kami_html5_dark.css"],
    'light': ['responsive.css', "kami_html5.css"] }

WRITER_NAME = 'html5'

DEFAULT_FILTERS = {
        'rst': r'.+\.rst',
        'md': r'.+\.md'}



from pathlib import Path

PUBLISHER_VERSION_APPENDIX_PATH = (Path(__file__).parent
        / 'assets' / 'publisher_version_appendix.html').resolve()


from sys import stderr, stdout
import re
import os
import logging
import errno


class CustomizedLogHandler(logging.Handler):

    def emit(self, record):
        target = stderr if record.levelno >= logging.ERROR else stdout
        print_content = "{} {}".format(record.levelname, record.msg)

        print(print_content, file=target)


class ParserMarkupLanguageDict(dict):  # TODO docstring

    def initialize(self, is_source_single_file):
        logger = logging.getLogger(PROGRAM_NAME)

        # empty all entry with value is None
        for key, value in self.copy().items():
            if value is None:
                self.pop(key)

        # single mode & web server mode can not have 2~ language opn
        if is_source_single_file and len(self) > 1:
            logger.critical(
    "more than 1 markup langauge option is given in single/web server mode")
            exit(errno.EINVAL)

        for langauge, filters in self.items():
            if len(filters) == 0:
                # empty list, i.e. option given but 0 filters provided
                # give it default filter of this langauge
                default_filter = DEFAULT_FILTERS[langauge]
                self[langauge].append(default_filter)

            else:  # test each filter to be legal
                for fil in filters:
                    try:
                        re.compile(fil)
                    except re.error:
                        logger.critical(
        'option --{} gets an illegal regex pattern: {}'.format(langauge, fil))
                        exit(errno.EINVAL)


def normalize_src_arg_and_test_access(src_arg):
    """
    - used in single mode & web server mode
    - normalize (i.e. find full path of) SOURCE arg
    - test read access to the file; log critical if failed to do so
    """
    # normalize source path
    src_path = os.path.realpath(src_arg)

    # test SOURCE file
    try:
        open(src_path, 'r')
    except OSError as err:
        logging.getLogger(PROGRAM_NAME).critical(
                "re {} of SOURCE: {}"
                .format(src_arg, err.strerror))
        exit(err.errno)

    return src_path


def create_settings_overrides(render_preset):
    logging.getLogger(PROGRAM_NAME).debug(
            'render_preset={}'.format(render_preset))

    settings_overrides = {}
    settings_overrides["stylesheet_dirs"] = \
            [(Path(__file__).parent / "assets" / "stylesheets").resolve()]
            # ./assets/stylesheets

    settings_overrides["stylesheet_path"] = \
            PRESETS_STYLESHEET_PATHS[render_preset]

    return settings_overrides


def append_publisher_version_to_file(file_path):
    try:
        with (open(PUBLISHER_VERSION_APPENDIX_PATH, 'r') as appendix_file,
                open(file_path, 'a') as  working_file):
            appendix = appendix_file.read()
            working_file.write(appendix)

    except OSError as err:
        logging.getLogger(PROGRAM_NAME).error(
                'fail to append publisher version, {}: {}'.format(
                        err.filename, err.strerror))
