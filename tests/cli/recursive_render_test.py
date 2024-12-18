"""
test recursive mode of cli
"""


import tempfile
import os

from single_render_test import run_single_mode, assert_good_rst_render
from get_filepaths import \
        copy_rst_recursive1_to, copy_rst_recursive2_to, copy_rst_recursive3_to


def run_recursive_mode(*args):
    return run_single_mode('--recursive', *args)


def _find_subfiles_recursively(root):
    entries = []
    for dirpath, _, filesnames in os.walk(root):
        for filename in filesnames:
            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, root)
            entry = (full_path, rel_path)
            entries.append(entry)
    return entries


class TestRender:  #  yes DESTINATION, no suffix

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            copy_rst_recursive1_to(src_dir)

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            src_entries = _find_subfiles_recursively(src_dir)
            dest_entries = _find_subfiles_recursively(dest_dir)

            # BUG
            assert len(src_entries) == len(dest_entries)

    def test2(_):
        pass

    def test3(_):
        pass


class TestSuf:  #  yes DESTINATION, yes suffix
    pass  # TODO


class TestAlongside:  #  no DESTINATION, no suffix
    pass  # TODO


class TestAlongsideSuf:  #  no DESTINATION, yes suffix
    pass  # TODO



# TODO overwritting warning