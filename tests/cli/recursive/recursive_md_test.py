

import tempfile
import os

from ... import TesteeDir
from .. import MD_FLAG, EXPR_FLAG, run_recursive_mode, assert_succ_render


class TestMdExtensionSingle:  # w/ --md and single filter in extension

    def test1(_):
        with (TesteeDir('md_simple') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [MD_FLAG, 'md']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)


    def test2(_):
        with (TesteeDir('md_comprehensive') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [MD_FLAG, 'md']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

    def test3(_):
        with (TesteeDir('md_extended') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [MD_FLAG, 'md']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)


class TestMdArgRegex:  # given --md and filter in regex form (-e)

    def test1(_):
        with (TesteeDir('md_simple') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [MD_FLAG, r'.+\.md', EXPR_FLAG]

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

    def test2(_):
        with (TesteeDir('md_comprehensive') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [MD_FLAG, r'.+\.md', EXPR_FLAG]

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

    def test3(_):
        with (TesteeDir('md_extended') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [MD_FLAG, r'.+\.md', EXPR_FLAG]

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

