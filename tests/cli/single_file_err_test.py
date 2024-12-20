"""
test single mode of cli, file related err
"""


import tempfile
import os
import shutil
import re
from pathlib import Path

from cli_test_shared import SUFFIX_FLAG, rst_simple, run_single_mode


class TestSrcFileErr:  # err related source file

    def test_src_no_exs(_):  # issue with SOURCE arg
        with tempfile.TemporaryDirectory() as temp_dir:
            src = (Path(temp_dir) / 'non_exs_file.rst').resolve()
            dest = (Path(temp_dir) / 'output.html').resolve()
            result = run_single_mode(src, dest)
            assert result.returncode == 2
            assert re.match(
                    r'CRITICAL re .+ of SOURCE: No such file or directory',
                    result.stderr)

    def test_src_is_dir(_):
        with tempfile.TemporaryDirectory() as temp_dir:
            src = Path(temp_dir).resolve()
            dest = (Path(temp_dir) / 'output.html').resolve()
            result = run_single_mode(src, dest)
            assert result.returncode == 21
            assert re.match(
                    r'CRITICAL re .+ of SOURCE: Is a directory',
                    result.stderr)

    def test_src_no_perm(_):
        with (tempfile.TemporaryDirectory() as temp_dir,
                tempfile.NamedTemporaryFile(delete=True) as temp_file):
            dest = (Path(temp_dir) / 'output.html').resolve()

            src = temp_file.name
            os.chmod(temp_file.name, 0o133)  # no permission

            result = run_single_mode(src, dest)
            assert result.returncode == 13
            assert re.match(
                    r'CRITICAL re .+ of SOURCE: Permission denied',
                    result.stderr)


class TestDestFileErr:  # issue w/ destination

    def test_non_exs(_):  # given DESTINATION, not suffix
        with tempfile.TemporaryDirectory() as temp_dir:
            src = rst_simple

            dest = os.path.realpath(os.path.join(
                    temp_dir, 'non_exist_dir', 'output.html'))

            result = run_single_mode(src, dest)
            assert result.returncode == 2
            assert re.match(
    r'CRITICAL re .+ of DESTINATION: No such file or directory',
                    result.stderr)

    def test_is_dir(_):
        with tempfile.TemporaryDirectory() as temp_dir:
            src = rst_simple

            result = run_single_mode(src, temp_dir)
            assert result.returncode == 21
            assert re.match(
                    r'CRITICAL re .+ of DESTINATION: Is a directory',
                    result.stderr)

    def test_no_perm(_):
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            src = rst_simple

            dest = temp_file.name
            os.chmod(dest, 0o555)  # no write perm

            result = run_single_mode(src, dest)
            assert result.returncode == 13
            assert re.search(
                    r'CRITICAL re .+ of DESTINATION: Permission denied',
                    result.stderr)

    def test_alongside_no_perm(_):  # no given DESTINATION, not suffix
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.realpath(os.path.join(temp_dir, 'ipt.rst'))
            shutil.copy2(rst_simple, src)

            dest = os.path.realpath(os.path.join(temp_dir, 'ipt.html'))
            with open(dest, 'w'):  # create empty file
                pass
            os.chmod(dest, 0o555)  # no write perm

            result = run_single_mode(src)  # no DESTINATION
            assert result.returncode == 13
            assert re.search(
                    r'CRITICAL can not create destination: .+',
                    result.stderr)

    def test_suffix_no_perm(_):
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.realpath(os.path.join(temp_dir, 'ipt.rst'))
            shutil.copy2(rst_simple, src)

            dest = os.path.realpath(os.path.join(temp_dir, 'ipt_suf.html'))
            with open(dest, 'w'):  # create empty file
                pass
            os.chmod(dest, 0o555)  # no write perm
            # no DESTINATION, with suffix
            result = run_single_mode(src, SUFFIX_FLAG, '_suf')
            assert result.returncode == 13
            assert re.search(
                    r'CRITICAL can not create destination: .+',
                    result.stderr)