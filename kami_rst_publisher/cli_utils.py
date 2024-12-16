"""
common utility functions used in CLI
"""


# stylesheets in STYLESHEET_DIR
STYLESHEET_PATHS = {
    'light': ["publisher_version.css", 'responsive.css', "kami_html5.css"],
    'dark': ["publisher_version.css", 'responsive.css', "kami_html5.css",
            "kami_html5_dark.css"]
}


from pathlib import Path


def determine_parser():
    return 'restructuredtext'  # TODO


def create_settings_overrides(render_preset):
    settings_overrides = {}

    settings_overrides["stylesheet_dirs"] = \
            [(Path(__file__).parent / "assets" / "stylesheets").resolve()]
            # ./assets/stylesheets

    settings_overrides["stylesheet_path"] = STYLESHEET_PATHS[render_preset]

    return settings_overrides
