"""
implment recursive mode of kami_rst_publisher CLI
"""


import logging
import os
import re
import errno

from docutils.core import publish_file

from .cli_single import RENDERED_FILE_EXTENSION
from .cli_utils import PROGRAM_NAME, WRITER_NAME, \
        create_settings_overrides, \
        append_publisher_version_to_file


def cli_recursive_mode_main(src_arg, dest_arg,
        suffix, mlo_config, render_preset):
    # cache for used in _handle_os_walk_err
    global src_root_cache
    global src_arg_cache
    src_arg_cache = src_arg

    global stat
    stat = {'skip_file': 0, 'new_file': 0, 'overwrite_file': 0, 'new_folder': 0}

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
    src_file_paths, src_file_relpaths, parsers_names, err_no = \
            _create_src_file_paths_and_rel2root(src_root, mlo_config)

    # create a list of dest_file_path
    dest_file_paths, dest_file_relpaths = _create_dest_file_paths(
            src_file_relpaths, dest_root, suffix)

    debug_log_path_prefix = "paths created & parsers:\n"

    debug_log_path_content = \
"""{} -{}-> {}
\t  {}
\t->{}"""
    logger.debug(debug_log_path_prefix + '\n'.join(
            debug_log_path_content.format(*paths) for paths
            in zip(src_file_relpaths, parsers_names, dest_file_relpaths,
                    src_file_paths, dest_file_paths)))

    logger.debug('test & create destination directory structure')

    err_no = _test_dest_dirs_access(dest_file_paths, dest_root) or err_no
    dest_file_paths, en_opt = _test_dest_files_write(
            dest_file_paths, dest_file_relpaths, dest_root)
    err_no = en_opt or err_no

    logger.debug('publish html files')
    _publish_per_file(render_preset,
        src_file_paths, src_file_relpaths,
        dest_file_paths, dest_file_relpaths)

    stat['discover_file'] = len(src_file_paths)
    stat['publish_file'] = stat['new_file'] + stat['overwrite_file']
    # log stat
    logger.info("""finish statistics:
discover files:\t{}
\tskip:\t{}
publish files:\t{}
\tnew:\t{}
\toverwrite:\t{}
new folders:\t{}""".format(
            stat['discover_file'], stat['skip_file'],
            stat['publish_file'], stat['new_file'], stat['overwrite_file'],
            stat['new_folder']))

    if stat['discover_file'] != stat['publish_file']:
        logger.error("fail to publish some files (publish {} < discover {})"
                .format(stat['publish_file'], stat['discover_file']))

    if stat['publish_file'] == 0:
        logger.warning('nothing published')

    logger.debug("finish: cli_recursive_mode_main")
    exit(err_no)


def _create_src_file_paths_and_rel2root(src_root, mlo_config):
    """
    - find all files recursively in ``src_root``
    - discover only files with read permission
    - generate their relative path to root (rel2root)
    - log info for permission denied during discovery
    """
    global logger
    global stat

    src_file_paths = []
    relpaths2root = []
    parsers_names = []
    err_no = 0

    # recursively discover files
    for dirpath, _, filesnames in os.walk(src_root,
            onerror=_handle_src_os_walk):
        for filename in filesnames:
            src = os.path.join(dirpath, filename)
            rel = os.path.relpath(src, src_root)
            test_result = _test_src_file_read(src, rel)

            parser = mlo_config.select_src_file_and_get_parser(
                    filename, rel)

            if not parser:
                # not matching expression arg
                logger.info("skip file: {}".format(rel))
                stat['skip_file'] += 1

            elif test_result == 0:
                # save the discover file only if can read from it
                src_file_paths.append(src)
                relpaths2root.append(rel)
                parsers_names.append(parser)
            else:
                err_no = test_result

    return src_file_paths, relpaths2root, parsers_names, err_no


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
    create a list 1f dest_file_path based on relative path, and consider ``suffix``
    """
    dest_file_paths = []
    dest_file_relpaths = []

    for rel_path in relpaths2root:
        rel_dir, full_filename = os.path.split(rel_path)
        filename, _  = os.path.splitext(full_filename)
        dest = os.path.abspath(os.path.join(
                dest_root, rel_dir,
                (filename + suffix + RENDERED_FILE_EXTENSION)))
        rel = os.path.relpath(dest, dest_root)

        dest_file_paths.append(dest)
        dest_file_relpaths.append(rel)

    return dest_file_paths, dest_file_relpaths


def _test_dest_dirs_access(dest_file_paths, dest_root):
    """
    test write permssion for folders in destination;
    create new folder if not existing in destination, will log as info
    """
    global stat
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
                stat['new_folder'] += 1

            except OSError:
                pass

        try:  # test access as a folder
            os.listdir(folder)
        except OSError as err:
            logger.error('destination folder {}: {}'.format(
                    rel_path, err.strerror))
            err_no = err.errno

    return err_no


def _test_dest_files_write(dest_file_paths, dest_file_relpaths, dest_root):
    """
    - test write permisssion for each file in dest_file_paths
    - create new file if not existing in destination
    - log warning if file already exists
    - log error if file can not be written
    - return a updated dest_file_paths, with inaccessible files removed
    """
    global stat
    global logger

    new_dest_file_paths = []
    err_no = 0

    for dest, rel in zip(dest_file_paths, dest_file_relpaths):
        # file existed before the write attempt
        file_existed = os.path.isfile(dest)

        try:
            open(dest, 'w')  # create / overwrite to dest
            if file_existed:
                logger.warning("overwrite: {}".format(rel))
                stat['overwrite_file'] += 1
            else:
                stat['new_file'] += 1

            new_dest_file_paths.append(dest)

        except OSError as err:
            logger.error('destination file {}: {}'.format(
                    rel, err.strerror))
            err_no = err.errno

    return new_dest_file_paths, err_no


def _publish_per_file(render_preset,
        src_file_paths, src_file_relpaths,
        dest_file_paths, dest_file_relpaths):
    """
    perform actual rendering of files by calling ``docutils.core.publish_file``
    """
    global logger

    # HACK parser_name=determine_parser(),
    parser_name = 'reStructuredText'
    settings_overrides=create_settings_overrides(render_preset)

    for src, src_rel, dest, dest_rel in zip(
            src_file_paths, src_file_relpaths,
            dest_file_paths, dest_file_relpaths):

        publish_file(source_path=src,
                destination_path=dest,
                parser_name=parser_name,
                writer_name=WRITER_NAME,
                settings_overrides=settings_overrides)

        append_publisher_version_to_file(dest)

        logger.info("publish: {}\t-> {}".format(src_rel, dest_rel))

