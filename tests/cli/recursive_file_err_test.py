"""
test recursive mode of cli, file related err
"""


import tempfile
import os
import re
import shutil

from recursive_render_test import run_recursive_mode
from get_filepaths import copy_rst_recursive2_to


class TestRoot:  # no permission to root

    def test_no_perm(_):  # no permission to root
        with tempfile.TemporaryDirectory() as temp_dir:
            root = os.path.join(temp_dir, 'root')
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


class TestSubfolder:  # warning with sub-folder

    def test1(_):
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.join(temp_dir, 'src')
            copy_rst_recursive2_to(src)
            dest = os.path.join(temp_dir, 'dest')

            os.chmod(src, 0o333)  # no read perm

            result = run_recursive_mode(src, dest)
            # TODO

            assert result.returncode == 13
            assert re.match( r'CRITICAL re .+ of SOURCE: Permission denied',
                    result.stderr)


class TestFiles:  # warning with files in sub-folders
    pass
