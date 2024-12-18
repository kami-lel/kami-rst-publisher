"""
implment single mode & recursive mode of kami_rst_publisher CLI
"""


RENDERED_FILE_EXTENSION = '.html'
DEFAULT_FILTER = r'.+\.rst'


import os
from sys import stderr
import logging

from docutils.core import publish_file

from .cli_utils import determine_parser, create_settings_overrides, \
        PROGRAM_NAME


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



def _handle_os_walk_err(err):
    """
    handle OSErrors raised during ``os.walk(root)`` in ``cli_recursive_mode_main``

    :param err:
    :type err: OSError
    """

    global root
    global src_arg_cache

    logger = logging.getLogger(PROGRAM_NAME)

    # os error related to root
    if err.filename == root:
        logger.critical('re {} of SOURCE: {}'
                .format(src_arg_cache, err.strerror))
        exit(err.errno)

    else:  # os error is related to sub-directory
        logger.warning('sub-directory {}: {}'
                .format(os.path.relpath(err.filename, root), err.strerror))
        # TODO write tests


def cli_recursive_mode_main(src_arg, dest_arg, expression_arg,
        suffix, render_preset, logger):
    # save as global to be used in _handle_os_walk_err
    global root
    global src_arg_cache
    src_arg_cache = src_arg

    logger.debug("start: recursive mode main\n\tsrc_arg={}".format(src_arg))

    root = os.path.realpath(src_arg)  # normalize
    logger.debug("root=normalized src_arg={}".format(root))

    src_paths = []
    dest_paths = []
    # discover all files in root
    for dirpath, _, filesnames in os.walk(
            root, onerror=_handle_os_walk_err):

        for filename in filesnames:
            src_path = os.path.join(dirpath, filename)
            try:  # test access of source files
                open(src_path, 'r')
            except OSError as err:
                logger.warning("file {}: {}"
                        .format(os.path.relpath(src_path, root), err.strerror))
                # TODO

            # print(dirpath, filename)


    logger.debug("finish: recursive mode main")