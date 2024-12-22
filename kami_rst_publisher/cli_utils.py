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
import logging

PUBLISHER_VERSION_APPENDIX_PATH = (Path(__file__).parent
        / 'assets' / 'publisher_version_appendix.html').resolve()

VERBOSITY2LOGGING_LEVEL = {
        -1: logging.CRITICAL + 1,  # -q
        0: logging.WARNING,
        1: logging.INFO,  # -v
        2: logging.DEBUG}  # -vv


from sys import stderr, stdout
import os


global logger
logger = logging.getLogger(PROGRAM_NAME)


class CustomizedLogHandler(logging.Handler):

    def emit(self, record):
        target = stderr if record.levelno >= logging.ERROR else stdout
        print_content = "{} {}".format(record.levelname, record.msg)

        print(print_content, file=target)


def normalize_src_arg_and_test_access(src_arg):
    """
    - used in single mode & web server mode
    - normalize (i.e. find full path of) SOURCE arg
    - test read access to the file; log critical if failed to do so
    """
    global logger

    # normalize source path
    src_path = os.path.realpath(src_arg)

    # test SOURCE file
    try:
        open(src_path, 'r')
    except OSError as err:
        logger.critical(
                "re {} of SOURCE: {}"
                .format(src_arg, err.strerror))
        exit(err.errno)

    return src_path


def create_settings_overrides(render_preset):
    global logger
    logger.debug(
            'render_preset={}'.format(render_preset))

    settings_overrides = {}
    settings_overrides["stylesheet_dirs"] = \
            [(Path(__file__).parent / "assets" / "stylesheets").resolve()]
            # ./assets/stylesheets

    settings_overrides["stylesheet_path"] = \
            PRESETS_STYLESHEET_PATHS[render_preset]

    return settings_overrides


def append_publisher_version_to_file(file_path):
    global logger

    try:
        with (open(PUBLISHER_VERSION_APPENDIX_PATH, 'r') as appendix_file,
                open(file_path, 'a') as  working_file):
            appendix = appendix_file.read()
            working_file.write(appendix)

    except OSError as err:
        logger.error(
                'fail to append publisher version, {}: {}'.format(
                        err.filename, err.strerror))
