"""
test recursive mode of cli, file related err
"""


import tempfile
import os
import re

from ... import TesteeDir
from .. import run_recursive_mode


class TestSrcRoot:  # no permission to source root

    def test_no_perm(_):  # no permission to root
        with (TesteeDir('rst_recursive2') as (root, _)):
            os.chmod(root, 0o333)  # no read perm

            result = run_recursive_mode(root)

            assert result.returncode == 13
            assert re.search( r'CRITICAL re .+ of SOURCE: Permission denied',
                    result.stderr)

    def test_no_exs(_):  # non exist
        with tempfile.TemporaryDirectory() as temp_dir:
            root = os.path.join(temp_dir, 'non_exist')

            result = run_recursive_mode(root)

            assert result.returncode == 2
            assert re.search(
                    r'CRITICAL re .+ of SOURCE: No such file or directory',
                    result.stderr)

    def test_file(_):  # is a file
        with tempfile.NamedTemporaryFile() as temp_file:
            result = run_recursive_mode(temp_file.name)

            assert result.returncode == 20
            assert re.search(
                    r'CRITICAL re .+ of SOURCE: Not a directory',
                    result.stderr)


class TestSrcSubfolder:  # warning with source subfolder

    def test1(_):
        with (TesteeDir('rst_recursive2') as (src, _),
                tempfile.TemporaryDirectory() as dest):

            bar = os.path.join(src, 'bar')
            os.chmod(bar, 0o333) # make src/bar no read perm

            result = run_recursive_mode(src, dest)
            assert result.returncode == 0
            assert re.search(r'WARNING source folder .+: Permission denied',
                    result.stdout)

    def test2(_):
        with (TesteeDir('rst_recursive3') as (src, _),
                tempfile.TemporaryDirectory() as dest):

            no_write = os.path.join(src, 'foo1', 'barbar', 'abc')
            os.chmod(no_write, 0o333) # make src/bar no read perm

            result = run_recursive_mode(src, dest)
            assert result.returncode == 0
            assert re.search(r'WARNING source folder .+: Permission denied',
                    result.stdout)


class TestSrcSubFiles:  # warning w/ source contained files

    def test1(_):
        with (TesteeDir('rst_recursive1') as (src, _),
                tempfile.TemporaryDirectory() as dest):

            no_write = os.path.join(src, 'bar.rst')
            os.chmod(no_write, 0o333) # make no read perm

            result = run_recursive_mode(src, dest)
            assert result.returncode == 13
            assert re.search(r'WARNING source file .+: Permission denied',
                    result.stdout)

    def test2(_):
        with (TesteeDir('rst_recursive2') as (src, _),
                tempfile.TemporaryDirectory() as dest):

            no_write = os.path.join(src, 'bar', 'abc.rst')
            os.chmod(no_write, 0o333) # make no read perm

            result = run_recursive_mode(src, dest)
            assert result.returncode == 13
            assert re.search(r'WARNING source file .+: Permission denied',
                    result.stdout)

