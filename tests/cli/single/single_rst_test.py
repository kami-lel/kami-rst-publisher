"""
test single mode of cli rendering rst
"""


import tempfile
import shutil
import os
import re

from .. import RST_FLAG, rst_simple, rst_comprehensive, rst_comprehensive2, \
        run_single_mode, assert_succ_render


class TestRenderMLO:  # with --rst

    def test1(_):  # use rst_simple
        with tempfile.NamedTemporaryFile() as temp_file:
            src = rst_simple
            dest = temp_file.name

            result = run_single_mode(src, dest, RST_FLAG)
            assert result.returncode == 0
            assert_succ_render(src, dest)

    def test2(_):  # use rst_comprehensive
        with tempfile.NamedTemporaryFile() as temp_file:
            src = rst_comprehensive
            dest = temp_file.name

            result = run_single_mode(src, dest, RST_FLAG)
            assert result.returncode == 0

            assert_succ_render(src, dest)

    def test3(_):  # use rst_comprehensive2
        with tempfile.NamedTemporaryFile() as temp_file:
            src = rst_comprehensive2
            dest = temp_file.name

            result = run_single_mode(src, dest, RST_FLAG)
            assert result.returncode == 0

            assert_succ_render(src, dest)


class TestRenderAuto:  # no MLO, thus automaticaly decide

    def test1(_):  # use rst_simple
        with tempfile.NamedTemporaryFile() as temp_file:
            src = rst_simple
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert_succ_render(src, dest)

    def test2(_):  # use rst_comprehensive
        with tempfile.NamedTemporaryFile() as temp_file:
            src = rst_comprehensive
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0

            assert_succ_render(src, dest)

    def test3(_):  # use rst_comprehensive2
        with tempfile.NamedTemporaryFile() as temp_file:
            src = rst_comprehensive2
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0

            assert_succ_render(src, dest)

    def test_cases1(_):  # extension e.g. .RST should also work
        with tempfile.TemporaryDirectory() as temp_dir:
            src_path = os.path.join(temp_dir, 'input.RST')
            dest_path = os.path.join(temp_dir, 'output.html')

            shutil.copy2(rst_simple, src_path)

            result = run_single_mode(src_path, dest_path)
            assert result.returncode == 0


class TestRenderAutoErr:  # errors when automatically decide

    def test_err1(_):  # can not auto decide b/c dont know extension
        with tempfile.TemporaryDirectory() as temp_dir:
            src_path = os.path.join(temp_dir, 'input.txt')
            dest_path = os.path.join(temp_dir, 'output.html')

            shutil.copy2(rst_simple, src_path)

            result = run_single_mode(src_path, dest_path)
            assert result.returncode == 22
            assert re.search(
    ('CRITICAL can not automatically decide markup language from '
    'extension \.txt of file:'), result.stderr)

    def test_err2(_):  # can not auto decide b/c dont know extension
        with tempfile.TemporaryDirectory() as temp_dir:
            src_path = os.path.join(temp_dir, 'input.aBc')
            dest_path = os.path.join(temp_dir, 'output.html')

            shutil.copy2(rst_simple, src_path)

            result = run_single_mode(src_path, dest_path)
            assert result.returncode == 22
            assert re.search(
    ('CRITICAL can not automatically decide markup language from '
    'extension \.aBc of file:'), result.stderr)

    def test_err3(_):  # can not auto decide b/c dont know extension
        with tempfile.TemporaryDirectory() as temp_dir:
            src_path = os.path.join(temp_dir, 'input')
            dest_path = os.path.join(temp_dir, 'output.html')

            shutil.copy2(rst_simple, src_path)

            result = run_single_mode(src_path, dest_path)
            assert result.returncode == 22
            assert re.search(
    ('CRITICAL can not automatically decide markup language from '
    'extension of file:'), result.stderr)

