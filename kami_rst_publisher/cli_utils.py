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


import pkg_resources
from pathlib import Path
from sys import stderr, stdout
import logging


def determine_parser():
    return 'restructuredtext'  # todo allow other formats


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


class CustomizedLogHandler(logging.Handler):

    def emit(self, record):
        target = stderr if record.levelno >= logging.ERROR else stdout
        print_content = "{} {}".format(record.levelname, record.msg)

        print(print_content, file=target)


def append_publisher_version_to_file(file_path):
    try:
        version = pkg_resources.get_distribution(PROGRAM_NAME).version
        ver_hf = version.replace('.', '-')  # change '3.1' -> '3-1
        with open(file_path, 'a') as file:
            file.write(VERSION_APPEND_TEMPLATE.format(ver_hf))

    except pkg_resources.DistributionNotFound:
        logging.getLogger(PROGRAM_NAME).error(
                'fail to append publisher version')

