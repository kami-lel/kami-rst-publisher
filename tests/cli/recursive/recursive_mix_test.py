

import os
import tempfile
import re

from ... import TesteeDir
from .. import RST_FLAG, MD_FLAG, EXPR_FLAG, VERBOSE_FLAG, \
        run_recursive_mode, assert_succ_render


class TestJustRst:  # only get rsts

    def test1(_):
        with (TesteeDir('mix') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *mlos, VERBOSE_FLAG)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, ext = os.path.splitext(rel)
                if filename and ext == '.rst':
                    dest = os.path.realpath(os.path.join(
                            dest_dir, filename + '.html'))
                    assert_succ_render(src, dest)

            assert len(re.findall(r'INFO skip file', result.stdout)) == 7
            assert len(re.findall(r'INFO publish', result.stdout)) == 11

    def test2(_):
        with (TesteeDir('mix') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [RST_FLAG, '.+\.rst', EXPR_FLAG]

            result = run_recursive_mode(src_dir, dest_dir, *mlos, VERBOSE_FLAG)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, ext = os.path.splitext(rel)
                if filename and ext == '.rst':
                    dest = os.path.realpath(os.path.join(
                            dest_dir, filename + '.html'))
                    assert_succ_render(src, dest)

            assert len(re.findall(r'INFO skip file', result.stdout)) == 7
            assert len(re.findall(r'INFO publish', result.stdout)) == 11


class TestJustMd:  # only get mds

    def test1(_):
        with (TesteeDir('mix') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [MD_FLAG, 'md']

            result = run_recursive_mode(src_dir, dest_dir, *mlos, VERBOSE_FLAG)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, ext = os.path.splitext(rel)
                if filename and ext == '.md':
                    dest = os.path.realpath(os.path.join(
                            dest_dir, filename + '.html'))
                    assert_succ_render(src, dest)

            assert len(re.findall(r'INFO skip file', result.stdout)) == 15
            assert len(re.findall(r'INFO publish', result.stdout)) == 3


class TestNoMLO:  # no MLO provided, thus run use default exts

    def test1(_):
        with (TesteeDir('mix') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            result = run_recursive_mode(src_dir, dest_dir, VERBOSE_FLAG)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, ext = os.path.splitext(rel)
                if filename and ext in ('.rst', '.md'):
                    dest = os.path.realpath(os.path.join(
                            dest_dir, filename + '.html'))
                    assert_succ_render(src, dest)

            assert len(re.findall(r'INFO skip file', result.stdout)) == 4
            assert len(re.findall(r'INFO publish', result.stdout)) == 14

