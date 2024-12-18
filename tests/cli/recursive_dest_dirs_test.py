"""
--recursive, test errors & info when dealing with destination dirs

i.e. test function of ``_test_create_dest_dirs`` in ``cli_recursive``
"""


import tempfile
import os
import re

from get_filepaths import \
        copy_rst_recursive1_to, copy_rst_recursive2_to, copy_rst_recursive3_to
from recursive_render_test import run_recursive_mode


class TestNewFodler:  # create new folders, copy tree like src

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir, 
                tempfile.TemporaryDirectory() as temp_dir):
            copy_rst_recursive1_to(src_dir)
            dest_dir = os.path.join(temp_dir, 'output')

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0
            finds = re.findall("INFO new folder in destination: .+",
                    result.stdout)
            assert len(finds) == 1
            assert os.path.isdir(dest_dir)

    def test2(_):
        with (tempfile.TemporaryDirectory() as src_dir, 
                tempfile.TemporaryDirectory() as dest_dir):
            copy_rst_recursive2_to(src_dir)

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0
            finds = re.findall("INFO new folder in destination: .+",
                    result.stdout)
            assert len(finds) == 2

            assert os.path.isdir(os.path.join(dest_dir, 'bar'))
            assert os.path.isdir(os.path.join(dest_dir, 'foo'))

    def test3(_):
        with (tempfile.TemporaryDirectory() as src_dir, 
                tempfile.TemporaryDirectory() as dest_dir):
            copy_rst_recursive3_to(src_dir)

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            finds = re.findall("INFO new folder in destination: .+",
                    result.stdout)
            assert len(finds) == 4

            assert os.path.isdir(os.path.join(dest_dir, 'bar'))
            assert os.path.isdir(os.path.join(dest_dir, 'foo'))
            assert os.path.isdir(os.path.join(dest_dir, 'foo1'))
            assert os.path.isdir(os.path.join(dest_dir, 'foo1', 'barbar'))
            assert os.path.isdir(os.path.join(
                    dest_dir, 'foo1', 'barbar', 'abc'))
            assert os.path.isdir(os.path.join(dest_dir, 'foo1', 'barbar2'))


class TestNoPerm:  # error when destination dirs no permission
    pass  # TODO


class TestIsFile:  # error when destination dirs is already a file
    pass  # TODO

