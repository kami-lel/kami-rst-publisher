"""
test recursive mode of cli related to option --suffix
"""


import tempfile
import os


from ... import TesteeDir
from .. import SUFFIX_FLAG, run_recursive_mode, assert_succ_render


class TestWithDest:  # with DESTINATION

    def test1(_):
        with (TesteeDir('rst_recursive1') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            suf = '_suf'
            result = run_recursive_mode(src_dir, dest_dir, SUFFIX_FLAG, suf)

            assert result.returncode == 0
            # check each file exists
            for src in src_files:
                src_rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(src_rel)
                dest = os.path.realpath(os.path.join(
                        dest_dir, filename + suf + '.html'))

                assert os.path.isfile(dest)
                assert_succ_render(src, dest)

    def test2(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            suf = '_suf'
            result = run_recursive_mode(src_dir, dest_dir, SUFFIX_FLAG, suf)

            assert result.returncode == 0
            # check each file exists
            for src in src_files:
                src_rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(src_rel)
                dest = os.path.realpath(os.path.join(
                        dest_dir, filename + suf + '.html'))

                assert os.path.isfile(dest)
                assert_succ_render(src, dest)

    def test_dft1(_):  # use default suffix
        with (TesteeDir('rst_recursive1') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            result = run_recursive_mode(src_dir, dest_dir, SUFFIX_FLAG)

            assert result.returncode == 0
            # check each file exists
            suf = '.R'
            # check each file exists
            for dir_name, _, files in os.walk(src_dir):
                for full_filename in files:
                    src = os.path.join(dir_name, full_filename)
                    src_rel = os.path.relpath(src, src_dir)
                    filename, _ = os.path.splitext(src_rel)
                    dest = os.path.realpath(os.path.join(
                            dest_dir, filename + suf + '.html'))

                    assert os.path.isfile(dest)
                    assert_succ_render(src, dest)


class TestNoDest:  # no DESTINATION

    def test1(_):
        with (TesteeDir('rst_recursive1') as (src_dir, src_files)):
            suf = '_suf'
            result = run_recursive_mode(src_dir, SUFFIX_FLAG, suf)

            assert result.returncode == 0
            # check each file exists
            for src in src_files:
                filename, _ = os.path.splitext(src)
                dest = filename + suf + '.html'
                assert os.path.isfile(dest)
                assert_succ_render(src, dest)

    def test2(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files)):
            suf = '_suf'
            result = run_recursive_mode(src_dir, SUFFIX_FLAG, suf)

            assert result.returncode == 0
            # check each file exists
            for src in src_files:
                filename, _ = os.path.splitext(src)
                dest = filename + suf + '.html'
                assert os.path.isfile(dest)
                assert_succ_render(src, dest)

    def test_dft1(_):  # use default suffix
        with (TesteeDir('rst_recursive1') as (src_dir, src_files)):
            suf = '.R'
            result = run_recursive_mode(src_dir, SUFFIX_FLAG, suf)

            assert result.returncode == 0
            # check each file exists
            for src in src_files:
                filename, _ = os.path.splitext(src)
                dest = filename + suf + '.html'
                assert os.path.isfile(dest)
                assert_succ_render(src, dest)
