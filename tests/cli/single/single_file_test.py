"""
test single mode of cli, file related
"""


import tempfile
import os
import re

from ... import TesteeDir
from .. import SUFFIX_FLAG, run_single_mode, assert_succ_render


class TestSuffix:  # test suffix when no DESTINATION

    def test1(_):  # customized suf
        with TesteeDir('rst_simple') as (src_dir, file_paths):
            src_file = file_paths[0]

            suf = '_suf'
            result = run_single_mode(src_file, SUFFIX_FLAG, suf)
            assert result.returncode == 0

            # supposed dest file location
            dest = os.path.realpath(os.path.join(
                    src_dir, 'rst_simple' + suf + '.html'))

            assert os.path.isfile(dest)  # created
            assert_succ_render(src_file, dest)

    def test_dft1(_):  # use default suffix
        with TesteeDir('rst_simple') as (src_dir, file_paths):
            src_file = file_paths[0]

            result = run_single_mode(src_file, SUFFIX_FLAG)
            assert result.returncode == 0

            suf = '.R'
            # supposed dest file location
            dest = os.path.realpath(os.path.join(
                    src_dir, 'rst_simple' + suf + '.html'))

            assert os.path.isfile(dest)  # created
            assert_succ_render(src_file, dest)


class TestOverwrite:   # tes overwriting warning

    def test1(_):
        with (TesteeDir('rst_simple') as (_, file_paths),
                tempfile.TemporaryDirectory() as dest_dir):

            src = file_paths[0]

            dest = os.path.realpath(os.path.join(
                    dest_dir, 'rst_simple.html'))
            with open(dest, 'w'):  # create empty file
                pass

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert re.match(r'WARNING overwrite: ', result.stdout)

    def test_alongside1(_):
        with (TesteeDir('rst_simple') as (src_dir, file_paths)):
            src = file_paths[0]
            dest = os.path.realpath(os.path.join(
                    src_dir, 'rst_simple.html'))

            with open(dest, 'w'):  # create empty file
                pass

            result = run_single_mode(src)
            assert result.returncode == 0
            assert re.match(r'WARNING overwrite: ', result.stdout)

    def test_suffix(_):
        with (TesteeDir('rst_simple') as (src_dir, file_paths)):
            src = file_paths[0]
            dest = os.path.realpath(os.path.join(
                    src_dir, 'rst_simple_suf.html'))

            with open(dest, 'w'):  # create empty file
                pass

            result = run_single_mode(src, SUFFIX_FLAG, '_suf')
            assert result.returncode == 0
            assert re.match(r'WARNING overwrite: ', result.stdout)

