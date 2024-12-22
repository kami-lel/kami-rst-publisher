"""
test single mode of cli, file related
"""


import tempfile
import os
import shutil
import re

from .. import SUFFIX_FLAG, run_single_mode, \
        rst_simple, rst_comprehensive


class TestOverwritting:  # test overwriting warning

    def test_normal(_):
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.realpath(os.path.join(temp_dir, 'ipt.rst'))
            shutil.copy2(rst_simple, src)

            dest = os.path.realpath(os.path.join(temp_dir, 'output.html'))
            with open(dest, 'w'):  # create empty file
                pass

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert re.match(r'WARNING overwrite: ', result.stdout)

    def test_alongside(_):
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.realpath(os.path.join(temp_dir, 'ipt.rst'))
            shutil.copy2(rst_simple, src)

            dest = os.path.realpath(os.path.join(temp_dir, 'ipt.html'))
            with open(dest, 'w'):  # create empty file
                pass

            result = run_single_mode(src)
            assert result.returncode == 0
            assert re.match(r'WARNING overwrite: ', result.stdout)

    def test_suffix(_):
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.realpath(os.path.join(temp_dir, 'ipt.rst'))
            shutil.copy2(rst_simple, src)

            dest = os.path.realpath(os.path.join(temp_dir, 'ipt_suf.html'))
            with open(dest, 'w'):  # create empty file
                pass

            result = run_single_mode(src, SUFFIX_FLAG, '_suf')
            assert result.returncode == 0
            assert re.match(r'WARNING overwrite: ', result.stdout)


class TestSuffix:  # test suffix option w/ no DESTINATION

    def test_dft1(_):  # use rst_simple
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.realpath(os.path.join(
                    temp_dir, 'ipt.rst'))
            shutil.copy2(rst_simple, src)

            suf = '.R'  # default

            result = run_single_mode(src, SUFFIX_FLAG)
            assert result.returncode == 0

            # supposed dest file location
            dest = os.path.realpath(os.path.join(
                    temp_dir, 'ipt' + suf + '.html'))

            assert os.path.isfile(dest)  # created


    def test_dft2(_):  # use rst_comprehensive
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.realpath(os.path.join(
                    temp_dir, 'ipt.rst'))
            shutil.copy2(rst_comprehensive, src)

            suf = '.R'  # default

            result = run_single_mode(src, SUFFIX_FLAG)
            assert result.returncode == 0

            # supposed dest file location
            dest = os.path.realpath(os.path.join(
                    temp_dir, 'ipt' + suf + '.html'))

            assert os.path.isfile(dest)  # created

            # assert each line in source file is present in output
            with (open(src, 'r') as ipt_file, open(dest, 'r') as dest_file):
                dest_read = dest_file.read()
                for line in ipt_file:
                    if line.isalpha():
                        assert line in dest_read

    def test1(_):  # use rst_simple & cutomized suf
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.realpath(os.path.join(
                    temp_dir, 'ipt.rst'))
            shutil.copy2(rst_simple, src)

            suf = '_suf'

            result = run_single_mode(src, SUFFIX_FLAG, suf)
            assert result.returncode == 0

            # supposed dest file location
            dest = os.path.realpath(os.path.join(
                    temp_dir, 'ipt' + suf + '.html'))

            assert os.path.isfile(dest)  # created


    def test2(_):  # use rst_comprehensive & cutomized suf
        with tempfile.TemporaryDirectory() as temp_dir:
            src = os.path.realpath(os.path.join(
                    temp_dir, 'ipt.rst'))
            shutil.copy2(rst_comprehensive, src)

            suf = 'abc'

            result = run_single_mode(src, SUFFIX_FLAG, suf)
            assert result.returncode == 0

            # supposed dest file location
            dest = os.path.realpath(os.path.join(
                    temp_dir, 'ipt' + suf + '.html'))

            assert os.path.isfile(dest)  # created

