"""
test recursive mode of cli
"""


import tempfile
import re
import os

from ... import TesteeDir
from .. import run_recursive_mode, VERBOSE_FLAG, assert_succ_render


class TestWarningNothingPublished:  # warning is logged when nothing published

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            assert re.search('WARNING nothing published', result.stdout)

    def test2(_):
        with (TesteeDir('txt') as (src_dir, _), 
                tempfile.TemporaryDirectory() as dest_dir):

            os.chmod(dest_dir, 0o333)

            result = run_recursive_mode(src_dir, dest_dir, VERBOSE_FLAG)

            assert result.returncode == 0
            assert len(re.findall(r'INFO skip file:', result.stdout)) == 2
            assert re.search('WARNING nothing published', result.stdout)

    def test3(_):
        with (TesteeDir('rst_simple') as (src_dir, _), 
                tempfile.TemporaryDirectory() as dest_dir):

            ban = os.path.join(src_dir, 'rst_simple.rst')
            os.chmod(ban, 0o000)

            result = run_recursive_mode(src_dir, dest_dir, VERBOSE_FLAG)

            assert result.returncode == 13
            assert re.search('WARNING nothing published', result.stdout)


class TestAlongside:  #  no DESTINATION

    def test1(_):
        with (TesteeDir('rst_recursive3') as (root, src_files)):

            result = run_recursive_mode(root)
            assert result.returncode == 0

            for src in src_files:
                filename, _ = os.path.splitext(src)
                dest = os.path.join(filename + '.html')
                assert_succ_render(src, dest)

