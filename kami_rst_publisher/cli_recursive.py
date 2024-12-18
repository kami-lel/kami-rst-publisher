"""
implment recursive mode of kami_rst_publisher CLI
"""


DEFAULT_FILTER = r'.+\.rst'


import logging
import os

from .cli_utils import PROGRAM_NAME


def cli_recursive_mode_main(src_arg, dest_arg, expression_arg,
        suffix, render_preset):
    # save as global to be used in _handle_os_walk_err
    global src_root
    global src_arg_cache
    src_arg_cache = src_arg

    logger = logging.getLogger(PROGRAM_NAME)
    logger.debug("start: recursive mode main\n\tsrc_arg={}".format(src_arg))

    src_root = os.path.realpath(src_arg)  # normalize
    logger.debug("src_root={}".format(src_root))

    dest_root = _determine_dest_root(dest_arg, src_root)

    # discover all files in root
    for dirpath, _, filesnames in os.walk(src_root,
            onerror=_handle_os_walk_err):
        for filename in filesnames:
            src_path = os.path.join(dirpath, filename)
            _render_per_src_file(src_path)

    logger.debug("finish: recursive mode main")


def _determine_dest_root(dest_arg, src_root):
    logger = logging.getLogger(PROGRAM_NAME)

    if dest_arg:
        dest_root = os.path.realpath(dest_arg)
        logger.debug("dest_root={}".format(dest_root))
    else:
        dest_root = src_root
        logger.debug("dest_root=src_root")

    return dest_root


def _handle_os_walk_err(err):
    """
    :param err:
    :type err: OSError
    """

    global src_root
    global src_arg_cache

    logger = logging.getLogger(PROGRAM_NAME)

    # os error related to root
    if err.filename == src_root:
        logger.critical('re {} of SOURCE: {}'
                .format(src_arg_cache, err.strerror))
        exit(err.errno)

    else:  # os error is related to sub-directory
        logger.warning('source sub-directory {}: {}'
                .format(os.path.relpath(err.filename, src_root), err.strerror))


def _render_per_src_file(src_path):
    relpath2root = os.path.relpath(src_path, src_root)

    _test_src_file_path_access(src_path, relpath2root)

    # TODO TODO working here


def _test_src_file_path_access(src_path, relpath2root):
    try:
        open(src_path, 'r')
    except OSError as err:
        logging.getLogger(PROGRAM_NAME).warning(
                "source file {}: {}".format(relpath2root, err.strerror))

