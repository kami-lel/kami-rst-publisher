"""
test single mode of cli rendering rst
"""


import tempfile
import shutil
import os
import re


from ... import TesteeDir
from .. import RST_FLAG, run_single_mode, assert_succ_render


class TestRenderMLO:  # with --rst

    def test1(_):  # use rst_simple
        with (TesteeDir('rst_simple') as (_, file_paths),
            tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest, RST_FLAG)
            assert result.returncode == 0
            assert_succ_render(src, dest)

    def test2(_):  # use rst_comprehensive
        with (TesteeDir('rst_comprehensive1') as (_, file_paths),
                tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest, RST_FLAG)
            assert result.returncode == 0

            assert_succ_render(src, dest)

    def test3(_):  # use rst_comprehensive2
        with (TesteeDir('rst_comprehensive1') as (_, file_paths),
                tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest, RST_FLAG)
            assert result.returncode == 0

            assert_succ_render(src, dest)


class TestRenderAuto:  # no MLO, thus automaticaly decide

    def test1(_):  # use rst_simple
        with (TesteeDir('rst_simple') as (_, file_paths),
            tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert_succ_render(src, dest)

    def test2(_):  # use rst_comprehensive
        with (TesteeDir('rst_comprehensive1') as (_, file_paths),
                tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0

            assert_succ_render(src, dest)

    def test3(_):  # use rst_comprehensive2
        with (TesteeDir('rst_comprehensive1') as (_, file_paths),
                tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0

            assert_succ_render(src, dest)

    def test_cases1(_):  # extension e.g. .RST should also work
        with (TesteeDir('rst_simple') as (src_dir, file_paths),
            tempfile.TemporaryDirectory() as dest_dir):

            src_old = file_paths[0]
            src_path = os.path.join(src_dir, 'input.RST')
            shutil.move(src_old, src_path)

            dest_path = os.path.join(dest_dir, 'output.html')

            result = run_single_mode(src_path, dest_path)
            assert result.returncode == 0


class TestRenderAutoErr:  # errors when automatically decide

    def test_err1(_):  # can not auto decide b/c dont know extension
        with (TesteeDir('rst_simple') as (src_dir, src_files),
            tempfile.TemporaryDirectory() as dest_dir):

            src_path = os.path.join(src_dir, 'input.txt')
            shutil.move(src_files[0], src_path)

            dest_path = os.path.join(dest_dir, 'output.html')

            result = run_single_mode(src_path, dest_path)
            assert result.returncode == 22
            assert re.search(
    ('CRITICAL can not automatically decide markup language from '
    'extension \.txt of file:'), result.stderr)

    def test_err2(_):  # can not auto decide b/c dont know extension
        with (TesteeDir('rst_simple') as (src_dir, src_files),
            tempfile.TemporaryDirectory() as dest_dir):

            src_path = os.path.join(src_dir, 'input.aBc')
            shutil.move(src_files[0], src_path)

            dest_path = os.path.join(dest_dir, 'output.html')


            result = run_single_mode(src_path, dest_path)
            assert result.returncode == 22
            assert re.search(
    ('CRITICAL can not automatically decide markup language from '
    'extension \.aBc of file:'), result.stderr)

    def test_err3(_):  # can not auto decide b/c dont know extension
        with (TesteeDir('rst_simple') as (src_dir, src_files),
            tempfile.TemporaryDirectory() as dest_dir):

            src_path = os.path.join(src_dir, 'input')
            shutil.move(src_files[0], src_path)

            dest_path = os.path.join(dest_dir, 'output.html')

            result = run_single_mode(src_path, dest_path)
            assert result.returncode == 22
            assert re.search(
    ('CRITICAL can not automatically decide markup language from '
    'extension of file:'), result.stderr)

