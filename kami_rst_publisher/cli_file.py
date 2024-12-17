"""
implment single mode & recursive mode of kami_rst_publisher CLI
"""


RENDERED_FILE_EXTENSION = '.html'
DEFAULT_FILTER = r'.+\.rst'


import os

from docutils.core import publish_file

from .cli_utils import determine_parser, create_settings_overrides


def cli_single_mode_main(src_arg, dest_arg,
        suffix, render_preset, logger):

    # normalize source path
    src_path = os.path.realpath(src_arg)

    # test SOURCE file
    try:
        open(src_path, 'r')
    except OSError as err:
        logger.critical("re {} of SOURCE: {}"
                .format(src_arg, err.strerror))
        exit(err.errno)

    # determine destination file path
    if dest_arg:
        # provided by DESTINATION arg, normalize path
        dest_path = os.path.realpath(dest_arg)

    else:  # save alongside SOURCE
        folder, full_filename = os.path.split(src_path)
        # split filename & extension
        filename, _ = os.path.splitext(full_filename)
        dest_path = os.path.join(folder, 
                (filename + suffix + RENDERED_FILE_EXTENSION))

    dest_info = dest_arg or dest_path  # used in print messgaes, etc.

    # test dest_path & create file if not existed
    if os.path.isfile(dest_path):
        logger.warning("overwrite: {}".format(dest_info))

    try:
        open(dest_path, 'w')
    except OSError as err:
        if dest_arg:
            err_msg = "re {} of DESTINATION: {}".format(
                    dest_info, err.strerror)
        else:
            err_msg = "can not create destination: {}".format(dest_info)

        logger.critical(err_msg)
        exit(err.errno)

    # perform render
    publish_file(source_path=src_arg,
            destination_path=dest_path,
            parser_name=determine_parser(),
            writer_name='html5',
            settings_overrides=create_settings_overrides(render_preset))

    logger.info("finish: {}\n\t->{}".format(src_arg, dest_info))


def cli_recursive_mode_main(src_arg, dest_arg, expression_arg,
        suffix, render_preset, logger):


    raise NotImplementedError  # TODO
