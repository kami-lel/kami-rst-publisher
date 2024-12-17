"""
implment single mode & recursive mode of kami_rst_publisher CLI
"""



from sys import exit, stderr

from docutils.core import publish_file


from .cli_utils import determine_parser, create_settings_overrides



def cli_single_mode_main(src_arg, dest_arg,
        suffix, render_preset, verbosity):

    # BUG require all kinds of test
    try:
        open(src_arg, 'r')
        open(dest_arg, 'w')
    except OSError as err:
        print("Error: {}".format(err), file=stderr)
        exit(err.errno)



    # TODO
    dest_arg = 'output.html'  # HACK

    publish_file(source_path=src_arg,
            destination_path=dest_arg,
            parser_name=determine_parser(),
            writer_name='html5',
            settings_overrides=create_settings_overrides(render_preset))



def cli_recursive_mode_main(src_arg, dest_arg,
        suffix, render_preset, verbosity):

    raise NotImplementedError  # TODO
