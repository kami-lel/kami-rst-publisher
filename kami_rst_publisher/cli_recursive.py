"""
implment recursive mode of kami_rst_publisher CLI
"""


DEFAULT_FILTER = r'.+\.rst'


import logging
import os

from .cli_single import RENDERED_FILE_EXTENSION
from .cli_utils import PROGRAM_NAME


def cli_recursive_mode_main(src_arg, dest_arg, expression_arg,
        suffix, render_preset):
    # cache for used in _handle_os_walk_err
    global src_root_cache
    global src_arg_cache
    src_arg_cache = src_arg

    logger = logging.getLogger(PROGRAM_NAME)

    src_root = src_root_cache = os.path.realpath(src_arg)  # normalize
    dest_root = os.path.realpath(dest_arg) if dest_arg else src_root

    logger.debug(
"""start: cli_recursive_mode_main
\tsrc_arg={}
\tsrc_root={}
\tdest_arg={}
\tdest_root={}""".format(src_arg, src_root, dest_arg, dest_root))

    src_file_paths = _find_src_files(src_root)

    # create a list of relative path
    relpaths2root = [os.path.relpath(v, src_root) for v in src_file_paths]

    _test_src_file_path(src_file_paths, relpaths2root)

    # create a list of dest_file_path
    dest_file_paths = _create_dest_file_paths(
            relpaths2root, dest_root, suffix)

    # logging generated lists
    for r, s, d in zip(relpaths2root, src_file_paths, dest_file_paths):
        logger.debug(
"""realpath2root=\t{}
\tsrc_file_path=\t{}
\tdest_file_path=\t{}""".format(r, s, d))

    err_no = _test_dest_dirs(dest_file_paths, dest_root)
    err_no = _test_dest_files(dest_file_paths, relpaths2root) or err_no

    # TODO actual perform render
    # TODO stat
    # TODO expression arg filter
    logger.debug("finish: recursive mode main")
    exit(err_no)


def _find_src_files(src_root):
    """
    find all files recursively in ``src_root``, return as a list of src file paths;
    also test read permission for folders in ``src_root``
    """
    src_file_paths = []

    for dirpath, _, filesnames in os.walk(src_root,
            onerror=_handle_src_os_walk):
        for filename in filesnames:
            src_file_path = os.path.join(dirpath, filename)
            src_file_paths.append(src_file_path)

    return src_file_paths


def _test_src_file_path(src_file_paths, relpaths2root):
    """
    given a list of source file pahts, ensure every file has read access permission
    """
    for src, rel in zip(src_file_paths, relpaths2root):
        try:
            open(src, 'r')
        except OSError as err:
            logging.getLogger(PROGRAM_NAME).warning(
                    'source file {}: {}'.format(rel, err.strerror))


def _handle_src_os_walk(err):
    """
    :param err:
    :type err: OSError
    """
    global src_root_cache
    global src_arg_cache

    logger = logging.getLogger(PROGRAM_NAME)

    # os error related to root
    if err.filename == src_root_cache:
        logger.critical('re {} of SOURCE: {}'
                .format(src_arg_cache, err.strerror))
        exit(err.errno)

    else:  # os error is related to sub-directory
        logger.warning('source folder {}: {}'.format(
                os.path.relpath(err.filename, src_root_cache), err.strerror))


def _create_dest_file_paths(relpaths2root, dest_root, suffix):
    """
    create a list of dest_file_path based on relative path, and consider ``suffix``
    """
    opt = []
    for rel_path in relpaths2root:
        rel_dir, full_filename = os.path.split(rel_path)
        filename, _  = os.path.splitext(full_filename)
        dest_file_path = os.path.abspath(os.path.join(
                dest_root, rel_dir,
                (filename + suffix + RENDERED_FILE_EXTENSION)))
        opt.append(dest_file_path)

    return opt


def _test_dest_dirs(dest_file_paths, dest_root):
    """
    test write permssion for folders in destination;
    create new folder if not existing in destination, will log as info
    """
    logger = logging.getLogger(PROGRAM_NAME)
    err_no = 0

    # find all folders
    dest_folders = []
    for dfp in dest_file_paths:
        folder, _ = os.path.split(dfp)
        if folder not in dest_folders:
            dest_folders.append(folder)

    for folder in dest_folders:
        rel_path =  os.path.relpath(folder, dest_root)
        # create if folder non existent
        if not os.path.exists(folder):
            try:
                os.makedirs(folder)
                logger.info("new folder in destination: {}".format(rel_path))
            except OSError:
                pass

        try:  # test access as a folder
            os.listdir(folder)
        except OSError as err:
            logger.error('destination folder {}: {}'.format(
                    rel_path, err.strerror))
            err_no = err.errno

    return err_no


def _test_dest_files(dest_file_paths, relpaths2root):
    """
    test write permssion for files in destination;
    create new file if not existing in destination;
    log warning if file already exists
    """
    logger = logging.getLogger(PROGRAM_NAME)
    err_no = 0

    for dest, rel in zip(dest_file_paths, relpaths2root):

        if os.path.isfile(dest):
            logger.warning("overwrite: {}".format(rel))

        try:
            open(dest, 'w')
        except OSError as err:
            logger.error('destination file {}: {}'.format(
                    rel, err.strerror))
            err_no = err.errno

    return err_no

