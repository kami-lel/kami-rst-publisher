"""
implment single mode of kami_rst_publisher CLI
"""


RENDERED_FILE_EXTENSION = '.html'
PUBLISH_FILE_WRITER_NAME = 'html5'


import os
import logging

from docutils.core import publish_file

from .cli_utils import PROGRAM_NAME, \
        determine_parser, create_settings_overrides, \
        append_publisher_version_to_file


def cli_single_mode_main(src_arg, dest_arg, suffix, render_preset):

    src_path = _normalize_src_path_and_test_access(src_arg)

    dest_path = _determine_dest_path(dest_arg, src_path, suffix)
    dest_info = dest_arg or dest_path  # used in print messgaes, etc.

    # test access to dest_path, and create the file if non-existent
    _test_dest_path_access(dest_path, dest_arg, dest_info)

    # perform render
    a = publish_file(source_path=src_arg,
            destination_path=dest_path,
            parser_name=determine_parser(),
            writer_name=PUBLISH_FILE_WRITER_NAME,
            settings_overrides=create_settings_overrides(render_preset))

    append_publisher_version_to_file(dest_path)

    logging.getLogger(PROGRAM_NAME).info(
            "finish: {}\n\t->{}".format(src_arg, dest_info))


def _normalize_src_path_and_test_access(src_arg):
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


def _determine_dest_path(dest_arg, src_path, suffix):
    # determine destination file path
    if dest_arg:
        # provided by DESTINATION arg, normalize path
        return os.path.realpath(dest_arg)

    else:  # save alongside SOURCE
        folder, full_filename = os.path.split(src_path)
        # split filename & extension
        filename, _ = os.path.splitext(full_filename)
        return os.path.join(folder,
                (filename + suffix + RENDERED_FILE_EXTENSION))


def _test_dest_path_access(dest_path, dest_arg, dest_info):
    logger = logging.getLogger(PROGRAM_NAME)

    if os.path.isfile(dest_path):
        logger.warning("overwrite: {}".format(dest_info))

    # test dest_path & create file if not existed
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

