"""
test recursive mode of cli, file related err
"""


import tempfile
import os
import re
import shutil

from recursive_render_test import run_recursive_mode
from get_filepaths import \
        copy_rst_recursive1_to, copy_rst_recursive2_to, copy_rst_recursive3_to


class TestSrcRoot:  # no permission to source root

    def test_no_perm(_):  # no permission to root
        with tempfile.TemporaryDirectory() as temp_dir:
            root = os.path.join(temp_dir, 'root')
            os.makedirs(root)
            copy_rst_recursive2_to(root)
            os.chmod(root, 0o333)  # no read perm

            result = run_recursive_mode(root)

            assert result.returncode == 13
            assert re.match( r'CRITICAL re .+ of SOURCE: Permission denied',
                    result.stderr)

    def test_no_exs(_):  # non exist
        with tempfile.TemporaryDirectory() as temp_dir:
            root = os.path.join(temp_dir, 'non_exist')

            result = run_recursive_mode(root)

            assert result.returncode == 2
            assert re.match(
                    r'CRITICAL re .+ of SOURCE: No such file or directory',
                    result.stderr)

    def test_file(_):  # is a file
        with tempfile.NamedTemporaryFile() as temp_file:
            result = run_recursive_mode(temp_file.name)

            assert result.returncode == 20
            assert re.match(
                    r'CRITICAL re .+ of SOURCE: Not a directory',
                    result.stderr)


class TestSrcSubfolder:  # warning with source subfolder

    def test1(_):
        with (tempfile.TemporaryDirectory() as src,
                tempfile.TemporaryDirectory() as dest):
            copy_rst_recursive2_to(src)

            bar = os.path.join(src, 'bar')
            os.chmod(bar, 0o333) # make src/bar no read perm

            result = run_recursive_mode(src, dest)
            assert result.returncode == 0
            assert re.match(r'WARNING sub-directory .+: Permission denied',
                    result.stderr)

    def test2(_):
        with (tempfile.TemporaryDirectory() as src,
                tempfile.TemporaryDirectory() as dest):
            copy_rst_recursive3_to(src)

            no_write = os.path.join(src, 'foo1', 'barbar', 'abc')
            os.chmod(no_write, 0o333) # make src/bar no read perm

            result = run_recursive_mode(src, dest)
            assert result.returncode == 0
            assert re.match(r'WARNING sub-directory .+: Permission denied',
                    result.stderr)


class TestSrcSubFiles:  # warning w/ source contained files

    def test1(_):
        with (tempfile.TemporaryDirectory() as src,
                tempfile.TemporaryDirectory() as dest):

            copy_rst_recursive1_to(src)

            no_write = os.path.join(src, 'bar.rst')
            os.chmod(no_write, 0o333) # make no read perm

            result = run_recursive_mode(src, dest)
            assert result.returncode == 0
            assert re.match(r'WARNING file .+: Permission denied',
                    result.stderr)

    def test2(_):
        with (tempfile.TemporaryDirectory() as src,
                tempfile.TemporaryDirectory() as dest):

            copy_rst_recursive2_to(src)

            no_write = os.path.join(src, 'bar', 'abc.rst')
            os.chmod(no_write, 0o333) # make no read perm

            result = run_recursive_mode(src, dest)
            assert result.returncode == 0
            assert re.match(r'WARNING file .+: Permission denied',
                    result.stderr)

