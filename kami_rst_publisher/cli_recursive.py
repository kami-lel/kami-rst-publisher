"""
implment recursive mode of kami_rst_publisher CLI
"""


DEFAULT_FILTER = r'.+\.rst'


import logging
import os

from docutils.core import publish_file

from .cli_single import RENDERED_FILE_EXTENSION, PUBLISH_FILE_WRITER_NAME
from .cli_utils import PROGRAM_NAME, \
        determine_parser, create_settings_overrides


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
    err_no = _test_dest_files(dest_file_paths, dest_root) or err_no
    _publish_files(render_preset, src_file_paths, dest_file_paths)

    # log stat
    logger.info("""finish: {} -> {},
\tdiscover files:\t{},
\tchange files:\t{}  ({} new + {} overwritten)
\tnew folders:\t{}""".format(
            src_arg, dest_root,
            len(src_file_paths),
            len(dest_file_paths), 0, 0,
            0))  # BUG

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


def _test_dest_files(dest_file_paths, dest_root):
    """
    test write permssion for files in destination;
    create new file if not existing in destination;
    log warning if file already exists
    """
    global stat_new_files_cnt
    global stat_overwritten_files_cnt
    logger = logging.getLogger(PROGRAM_NAME)
    err_no = 0

    for dest in dest_file_paths:
        rel = os.path.relpath(dest, dest_root)

        if os.path.isfile(dest):
            logger.warning("overwrite: {}".format(rel))
            stat_new_files_cnt -= 1
            stat_overwritten_files_cnt += 1

        try:
            open(dest, 'w')
            stat_new_files_cnt += 1
        except OSError as err:
            logger.error('destination file {}: {}'.format(
                    rel, err.strerror))
            err_no = err.errno

    return err_no


def _publish_files(render_preset, src_file_paths, dest_file_paths):
    """
    perform actual rendering of files by calling ``docutils.core.publish_file``
    """

    parser_name = determine_parser()
    settings_overrides=create_settings_overrides(render_preset)

    for src, dest in zip(src_file_paths, dest_file_paths):
        publish_file(source_path=src,
                destination_path=dest,
                parser_name=parser_name,
                writer_name=PUBLISH_FILE_WRITER_NAME,
                settings_overrides=settings_overrides)

