"""
common utility functions used in CLI
"""

PROGRAM_NAME = 'kami_rst_publisher'
PRESETS = ['dark', 'light']  # used in options -p choices
# stylesheets in STYLESHEET_DIR
PRESETS_STYLESHEET_PATHS = {
    'dark': ['responsive.css', "kami_html5.css",
            "kami_html5_dark.css"],
    'light': ['responsive.css', "kami_html5.css"] }

VERSION_APPEND_TEMPLATE = """
<!-- PUBLISHED BY kami_rst_publisher.#{} -->
"""

WRITER_NAME = 'html5'

PARSER_ARG2NAME = {
        'md': 'markdown',
        'rst': 'restructuredtext' }

EXTENSION2PARSER_NAME = {
        'md': 'markdown',
        'txt': 'markdown',
        'rst': 'restructuredtext'}

from pathlib import Path

SETUP_CFG_PATH = (Path(__file__).parent.parent / 'setup.cfg').resolve()




import configparser
from sys import stderr, stdout
import os
import logging


def determine_parser(src_file_path, markup_language_arg):
    if markup_language_arg is None:
        # auto determien by file extension
        _, extension = os.path.splitext(src_file_path)

    else:
        PARSER_ARG2NAME[markup_language_arg]



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
    config = configparser.ConfigParser()
    config.read(SETUP_CFG_PATH)

    try:
        version = config['metadata']['version']
        ver_hf = version.replace('.', '-')  # change e.g. '3.1' -> '3-1
        with open(file_path, 'a') as file:
            file.write(VERSION_APPEND_TEMPLATE.format(ver_hf))

    except KeyError:
        logging.getLogger(PROGRAM_NAME).error(
                'fail to append publisher version')
