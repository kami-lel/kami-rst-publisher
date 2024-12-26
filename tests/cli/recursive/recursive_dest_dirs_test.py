"""
--recursive, test errors & info when dealing with destination dirs

i.e. test function of ``_test_create_dest_dirs`` in ``cli_recursive``
"""


import tempfile
import os
import re

from ... import TesteeDir
from .. import run_recursive_mode, VERBOSE_FLAG


class TestNewFolder:  # create new folders, copy tree like src

    def test1(_):
        with (TesteeDir('rst_recursive1') as (src_dir, _),
                tempfile.TemporaryDirectory() as dest_parent):

            dest_dir = os.path.realpath(os.path.join(dest_parent, 'output'))

            result = run_recursive_mode(src_dir, dest_dir, VERBOSE_FLAG)
            assert result.returncode == 0
            finds = re.findall("INFO new folder in destination: .+",
                    result.stdout)
            assert len(finds) == 1
            assert os.path.isdir(dest_dir)

    def test2(_):
        with (TesteeDir('rst_recursive2') as (src_dir, _),
                tempfile.TemporaryDirectory() as dest_dir):

            result = run_recursive_mode(src_dir, dest_dir, VERBOSE_FLAG)
            assert result.returncode == 0
            finds = re.findall("INFO new folder in destination: .+",
                    result.stdout)
            assert len(finds) == 2

            assert os.path.isdir(os.path.join(dest_dir, 'bar'))
            assert os.path.isdir(os.path.join(dest_dir, 'foo'))

    def test3(_):
        with (TesteeDir('rst_recursive3') as (src_dir, _),
                tempfile.TemporaryDirectory() as dest_dir):

            result = run_recursive_mode(src_dir, dest_dir, VERBOSE_FLAG)
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

    def test1(_):
        with (TesteeDir('rst_recursive1') as (src_dir, _),
                tempfile.TemporaryDirectory() as dest_parent):

            dest_dir = os.path.join(dest_parent, 'output')

            os.makedirs(dest_dir)
            os.chmod(dest_dir, 0o000)  # no access

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 13
            assert re.search(
                    r'ERROR destination folder .+: Permission denied',
                    result.stderr)
            assert re.search('WARNING nothing published', result.stdout)


class TestIsFile:  # error when destination dirs is already a file

    def test1(_):
        with (TesteeDir('rst_recursive1') as (src_dir, _),
                tempfile.NamedTemporaryFile() as dest_file):

            result = run_recursive_mode(src_dir, dest_file.name)
            assert result.returncode == 20
            assert re.search(
                    r'ERROR destination folder .+: Not a directory',
                    result.stderr)

