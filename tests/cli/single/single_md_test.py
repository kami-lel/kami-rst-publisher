"""
test single mode of cli rendering md
"""


import tempfile

from ... import TesteeDir
from .. import MD_FLAG, run_single_mode, assert_succ_render


class TestRenderMLO:  # with --md

    def test1(_):
        with (TesteeDir('md_simple') as (_, file_paths),
            tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest, MD_FLAG)
            assert result.returncode == 0
            assert_succ_render(src, dest)

    def test2(_):
        with (TesteeDir('md_comprehensive') as (_, file_paths),
            tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest, MD_FLAG)
            assert result.returncode == 0
            assert_succ_render(src, dest)

    def test3(_):
        with (TesteeDir('md_extended') as (_, file_paths),
            tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest, MD_FLAG)
            assert result.returncode == 0
            assert_succ_render(src, dest)


class TestRenderAuto:  # no --md, thus automaticaly decide
    def test1(_):
        with (TesteeDir('md_simple') as (_, file_paths),
            tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert_succ_render(src, dest)

    def test2(_):
        with (TesteeDir('md_comprehensive') as (_, file_paths),
            tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert_succ_render(src, dest)

    def test3(_):
        with (TesteeDir('md_extended') as (_, file_paths),
            tempfile.NamedTemporaryFile() as temp_file):
            src = file_paths[0]
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert_succ_render(src, dest)

