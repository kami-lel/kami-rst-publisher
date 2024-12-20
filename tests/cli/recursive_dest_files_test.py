"""
--recursive, test errors & info when dealing with destination dirs

i.e. test function of ``_test_dest_files`` in ``cli_recursive``
"""


import tempfile
import shutil
import re
import os

from cli_test_shared import rst_simple,  run_recursive_mode


class TestOverwrite:  # test warning during overwrite

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            shutil.copy2(rst_simple, src_dir)
            open(os.path.join(dest_dir, 'rst_simple.html'), 'w')

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0
            assert re.search(r'WARNING overwrite: .+', result.stdout)


class TestNewFile:  # created files for writing

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            shutil.copy2(rst_simple, src_dir)
            dest_path = os.path.join(dest_dir, 'rst_simple.html')

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            assert os.path.isfile(dest_path)


class TestErrIsDir:  # file exists, but is a directory

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            shutil.copy2(rst_simple, src_dir)
            dest_path = os.path.join(dest_dir, 'rst_simple.html')
            os.makedirs(dest_path)

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 21
            assert re.search(r'ERROR destination file .+: Is a directory',
                    result.stderr)


class TestErrNoPerm:  # file exits, but no permission

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            shutil.copy2(rst_simple, src_dir)
            dest_path = os.path.join(dest_dir, 'rst_simple.html')
            open(dest_path, 'w')
            os.chmod(dest_path, 0o555)  # no write

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 13
            assert re.search(r'ERROR destination file .+: Permission denied',
                    result.stderr)

