"""
implment recursive mode of kami_rst_publisher CLI
"""


DEFAULT_FILTER = r'.+\.rst'


import logging
import os
import re

from docutils.core import publish_file

from .cli_single import RENDERED_FILE_EXTENSION, PUBLISH_FILE_WRITER_NAME
from .cli_utils import PROGRAM_NAME, \
        determine_parser, create_settings_overrides


def cli_recursive_mode_main(src_arg, dest_arg, filter,
        suffix, render_preset):
    # cache for used in _handle_os_walk_err
    global src_root_cache
    global src_arg_cache
    src_arg_cache = src_arg

    global stat_new_file_cnt
    global stat_overwrite_file_cnt
    global stat_new_folder_cnt
    stat_new_file_cnt = stat_overwrite_file_cnt = stat_new_folder_cnt = 0

    global logger
    logger = logging.getLogger(PROGRAM_NAME)
    logger.debug("start: cli_recursive_mode_main")

    # normalize root paths
    src_root = src_root_cache = os.path.realpath(src_arg)  # normalize
    dest_root = os.path.realpath(dest_arg) if dest_arg else src_root

    logger.debug(
"""args & roots:
src_arg=\t{}
src_root=\t{}
dest_arg=\t{}
dest_root=\t{}""".format(src_arg, src_root, dest_arg, dest_root))

    # discover & test files in source
    src_file_paths, relpaths2root, err_no = \
            _create_src_file_paths_and_rel2root(src_root, filter)

    # create a list of dest_file_path
    dest_file_paths = _create_dest_file_paths(
            relpaths2root, dest_root, suffix)

    logger.debug(
"""paths created:
(relpath2root\tsrc_file_path\tdest_file_path)
""" + '\n'.join('\t'.join(paths) for paths
            in zip(relpaths2root, src_file_paths, dest_file_paths)))

    logger.debug('test & create destination directory structure')

    err_no = _test_dest_dirs_access(dest_file_paths, dest_root) or err_no
    dest_file_paths, en_opt = _test_dest_files_write(dest_file_paths, dest_root)
    err_no = en_opt or err_no

    logger.debug('publish html files')
    _publish_files(render_preset, src_file_paths, dest_file_paths)

    stat_discover_files_cnt = len(src_file_paths)
    stat_change_files_cnt = stat_new_file_cnt + stat_overwrite_file_cnt
    # log stat
    logger.info("""finish recursive mode & stat:
discover raw files:\t{}
published files:\t{} ({} new + {} overwrite)
new folders:\t{}""".format(
            stat_discover_files_cnt,
            stat_change_files_cnt, stat_new_file_cnt, stat_overwrite_file_cnt,
            stat_new_folder_cnt))

    if stat_discover_files_cnt != stat_change_files_cnt:
        logger.error("fail to publish some files ({} < {})"
                .format(stat_change_files_cnt, stat_discover_files_cnt))

    logger.debug("finish: cli_recursive_mode_main")
    exit(err_no)


def _create_src_file_paths_and_rel2root(src_root, filter):
    """
    - find all files recursively in ``src_root``
    - discover only files with read permission
    - generate their relative path to root (rel2root)
    - log info for permission denied during discovery
    """
    global logger

    src_file_paths = []
    relpaths2root = []
    err_no = 0

    # TODO test expression arg function
    # TODO test skip non-matching logging

    # recursively discover files
    for dirpath, _, filesnames in os.walk(src_root,
            onerror=_handle_src_os_walk):
        for filename in filesnames:
            src = os.path.join(dirpath, filename)
            rel = os.path.relpath(src, src_root)
            test_result = _test_src_file_read(src, rel)

            if not re.fullmatch(filter, filename):
                # not matching expression arg
                logger.info("skip source file: {}".format(rel))
            elif test_result == 0:
                # save the discover file only if can read from it
                src_file_paths.append(src)
                relpaths2root.append(rel)
            else:
                err_no = test_result

    return src_file_paths, relpaths2root, err_no


def _handle_src_os_walk(err):
    """
    :param err:
    :type err: OSError
    """
    global src_root_cache
    global src_arg_cache
    global logger

    # os error related to root
    if err.filename == src_root_cache:
        logger.critical('re {} of SOURCE: {}'
                .format(src_arg_cache, err.strerror))
        exit(err.errno)

    else:  # os error is related to sub-directory
        logger.warning('source folder {}: {}'.format(
                os.path.relpath(err.filename, src_root_cache), err.strerror))


def _test_src_file_read(src_file_path, relpath2root):
    """
    test read permission of a single src_path file, log warnning if failed to read
    """
    try:
        open(src_file_path, 'r')
        return 0

    except OSError as err:
        logging.getLogger(PROGRAM_NAME).warning(
                'source file {}: {}'.format(relpath2root, err.strerror))
        return err.errno


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


def _test_dest_dirs_access(dest_file_paths, dest_root):
    """
    test write permssion for folders in destination;
    create new folder if not existing in destination, will log as info
    """
    global stat_new_folder_cnt
    global logger
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
                stat_new_folder_cnt += 1

            except OSError:
                pass

        try:  # test access as a folder
            os.listdir(folder)
        except OSError as err:
            logger.error('destination folder {}: {}'.format(
                    rel_path, err.strerror))
            err_no = err.errno

    return err_no


def _test_dest_files_write(dest_file_paths, dest_root):
    """
    - test write permisssion for each file in dest_file_paths
    - create new file if not existing in destination
    - log warning if file already exists
    - log error if file can not be written
    - return a updated dest_file_paths, with inaccessible files removed
    """
    global stat_new_file_cnt
    global stat_overwrite_file_cnt
    global logger

    new_dest_file_paths = []
    err_no = 0

    for dest in dest_file_paths:
        rel = os.path.relpath(dest, dest_root)

        # file existed before the write attempt
        file_existed = os.path.isfile(dest)

        try:
            open(dest, 'w')  # create / overwrite to dest
            if file_existed:
                logger.warning("overwrite: {}".format(rel))
                stat_overwrite_file_cnt += 1
            else:
                stat_new_file_cnt += 1

            new_dest_file_paths.append(dest)

        except OSError as err:
            logger.error('destination file {}: {}'.format(
                    rel, err.strerror))
            err_no = err.errno

    return new_dest_file_paths, err_no


def _publish_files(render_preset, src_file_paths, dest_file_paths):
    """
    perform actual rendering of files by calling ``docutils.core.publish_file``
    """

    parser_name = determine_parser()
    settings_overrides=create_settings_overrides(render_preset)

    # TODO infor per publish

    for src, dest in zip(src_file_paths, dest_file_paths):
        publish_file(source_path=src,
                destination_path=dest,
                parser_name=parser_name,
                writer_name=PUBLISH_FILE_WRITER_NAME,
                settings_overrides=settings_overrides)

