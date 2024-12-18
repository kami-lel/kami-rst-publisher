"""
common utility functions used in CLI
"""


PROGRAM_NAME = 'kami_rst_publisher'
PRESETS = ['dark', 'light']  # used in options -p choices
# stylesheets in STYLESHEET_DIR
PRESETS_STYLESHEET_PATHS = {
    'dark': ["publisher_version.css", 'responsive.css', "kami_html5.css",
            "kami_html5_dark.css"],
    'light': ["publisher_version.css", 'responsive.css', "kami_html5.css"] }


from pathlib import Path
from sys import stderr, stdout
import logging


def determine_parser():
    return 'restructuredtext'  # TODO allow other formats


def create_settings_overrides(render_preset):
    settings_overrides = {}

    settings_overrides["stylesheet_dirs"] = \
            [(Path(__file__).parent / "assets" / "stylesheets").resolve()]
            # ./assets/stylesheets

    settings_overrides["stylesheet_path"] = \
            PRESETS_STYLESHEET_PATHS[render_preset]

    return settings_overrides


class CustomizedLogHandler(logging.Handler):

    def emit(self, record):
        target = stderr if record.levelno >= logging.WARNING else stdout
        print_content = "{} {}".format(record.levelname, record.msg)

        print(print_content, file=target)

