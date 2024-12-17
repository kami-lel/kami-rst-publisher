"""
implment single mode & recursive mode of kami_rst_publisher CLI
"""




from docutils.core import publish_file


from .cli_utils import determine_parser, create_settings_overrides


def cli_single_mode_main(
        src_file, dest_file, suffix, render_preset, verbosity):
    pass  # TODO implement single mode



def cli_recursive_mode_main(
        src_path, dest_path, suffix, render_preset, verbosity):
    pass  # TODO implement recursive

