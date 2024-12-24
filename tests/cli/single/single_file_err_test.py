"""
test single mode of cli, file related err
"""


import tempfile
import os
import shutil
import re
from pathlib import Path

from ... import TesteeDir
from .. import SUFFIX_FLAG, run_single_mode


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
        with (TesteeDir('rst_simple') as (_, file_paths),
                tempfile.TemporaryDirectory() as temp_dir):
            src = file_paths[0]

            dest = os.path.realpath(os.path.join(
                    temp_dir, 'non_exist_dir', 'output.html'))

            result = run_single_mode(src, dest)
            assert result.returncode == 2
            assert re.match(
    r'CRITICAL re .+ of DESTINATION: No such file or directory',
                    result.stderr)

    def test_is_dir(_):
        with (TesteeDir('rst_simple') as (_, file_paths),
                tempfile.TemporaryDirectory() as temp_dir):
            src = file_paths[0]

            result = run_single_mode(src, temp_dir)
            assert result.returncode == 21
            assert re.match(
                    r'CRITICAL re .+ of DESTINATION: Is a directory',
                    result.stderr)

    def test_no_perm(_):
        with (TesteeDir('rst_simple') as (_, file_paths),
                tempfile.NamedTemporaryFile(delete=True) as temp_file):
            src = file_paths[0]

            dest = temp_file.name
            os.chmod(dest, 0o555)  # no write perm

            result = run_single_mode(src, dest)
            assert result.returncode == 13
            assert re.search(
                    r'CRITICAL re .+ of DESTINATION: Permission denied',
                    result.stderr)

    def test_alongside_no_perm(_):  # no given DESTINATION, not suffix
        with (TesteeDir('rst_simple') as (temp_dir, file_paths)):
            src = file_paths[0]

            dest = os.path.realpath(os.path.join(
                    temp_dir, 'rst_simple.html'))
            with open(dest, 'w'):  # create empty file
                pass

            os.chmod(dest, 0o555)  # no write perm

            result = run_single_mode(src)  # no DESTINATION
            assert result.returncode == 13
            assert re.search(
                    r'CRITICAL can not create destination: .+',
                    result.stderr)

    def test_suffix_no_perm(_):
        with (TesteeDir('rst_simple') as (temp_dir, file_paths)):
            src = file_paths[0]

            dest = os.path.realpath(os.path.join(
                    temp_dir, 'rst_simple_suf.html'))
            with open(dest, 'w'):  # create empty file
                pass
            os.chmod(dest, 0o555)  # no write perm
            # no DESTINATION, with suffix
            result = run_single_mode(src, SUFFIX_FLAG, '_suf')
            assert result.returncode == 13
            assert re.search(
                    r'CRITICAL can not create destination: .+',
                    result.stderr)