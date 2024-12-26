

import tempfile
import os
import re


from ... import TesteeDir
from .. import  RST_FLAG, EXPR_FLAG, VERBOSE_FLAG, \
        run_recursive_mode, assert_succ_render, \
        change_files_extension_recursively


class TestRstExtensionSingle:  # w/ --rst and single filter in extension

    def test_rst1(_):
        with (TesteeDir('rst_recursive1') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

    def test_rst2(_):
        with (TesteeDir('rst_recursive2') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

    def test_rst3(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)


class TestRstExtensionCasing:  # extension is case-insensitive

    def test_lettercase1(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):
            new_ext = 'Rst'
            change_files_extension_recursively(src_dir, new_ext)

            mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for old_src in src_files:
                rel = os.path.relpath(old_src, src_dir)
                filename, _ = os.path.splitext(rel)
                new_src = os.path.join(src_dir, filename + '.' + new_ext)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(new_src, dest)

    def test_lettercase2(_):  # with weird letter cases
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):
            new_ext = 'RST'
            change_files_extension_recursively(src_dir, new_ext)

            mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for old_src in src_files:
                rel = os.path.relpath(old_src, src_dir)
                filename, _ = os.path.splitext(rel)
                new_src = os.path.join(src_dir, filename + '.' + new_ext)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(new_src, dest)



class TestRstExtensionCustomized:

    def test_txt1(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):
            new_ext = 'txt'
            change_files_extension_recursively(src_dir, new_ext)

            mlos = [RST_FLAG, 'txt']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for old_src in src_files:
                rel = os.path.relpath(old_src, src_dir)
                filename, _ = os.path.splitext(rel)
                new_src = os.path.join(src_dir, filename + '.' + new_ext)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(new_src, dest)
 
    def test_txt2(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):
            new_ext = 'tXt'
            change_files_extension_recursively(src_dir, new_ext)

            mlos = [RST_FLAG, 'txt']

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for old_src in src_files:
                rel = os.path.relpath(old_src, src_dir)
                filename, _ = os.path.splitext(rel)
                new_src = os.path.join(src_dir, filename + '.' + new_ext)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(new_src, dest)


class TestRstExtensionSelect:  # use --rst extension to filter

    def test_select1(_):  # only part of the file should be rendered
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            split = 3

            for src in src_files[:split]:
                # append .txt as their new extension
                new_src = src + '.txt'
                os.rename(src, new_src)

            mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *mlos, VERBOSE_FLAG)
            assert result.returncode == 0

            for src in src_files[split:]:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

            assert len(re.findall(r'INFO skip file:', result.stdout)) == 3

    def test_select2(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            split = 3

            for src in src_files[split:]:
                # append .txt as their new extension
                new_src = src + '.txt'
                os.rename(src, new_src)


            mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *mlos, VERBOSE_FLAG)
            assert result.returncode == 0

            for src in src_files[:split]:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

            assert len(re.findall(r'INFO skip file:', result.stdout)) == 8

    def test_select3(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            split = 7

            for src in src_files[:split]:
                # append .txt as their new extension
                new_src = src + '.txt'
                os.rename(src, new_src)

            mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *mlos, VERBOSE_FLAG)
            assert result.returncode == 0

            for src in src_files[split:]:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

            assert len(re.findall(r'INFO skip file:', result.stdout)) == 7

    def test_multiple_extension1(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            rsts = src_files[:5]
            txts = src_files[5:8]
            abcs = src_files[8:]

            cache = []
            for src in txts:
                new_src = src + '.txt'
                os.rename(src, new_src)
                cache.append(new_src)
            txts = cache

            cache = []
            for src in abcs:
                new_src = src + '.abc'
                os.rename(src, new_src)
                cache.append(new_src)
            abcs = cache

            mlos = [RST_FLAG, 'rst', 'txt']

            result = run_recursive_mode(src_dir, dest_dir, *mlos, VERBOSE_FLAG)
            assert result.returncode == 0

            for src in rsts:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

            for src in txts:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

            assert len(re.findall(r'INFO skip file:', result.stdout)) == 3


class TestRstArgRegex:  # given --rst and filter in regex form (-e)

    def test1(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            mlos = [RST_FLAG, r'.+\.rst', EXPR_FLAG]

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

    def test2(_):  # select only all upper cases
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            split = 5

            for src in src_files[:split]:
                # append .txt as their new extension
                new_src = src + '.RST'
                os.rename(src, new_src)


            mlos = [RST_FLAG, r'.+\.rst', EXPR_FLAG]

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in src_files[split:]:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

    def test_multiple_extension1(_):
        with (TesteeDir('rst_recursive3') as (src_dir, src_files),
                tempfile.TemporaryDirectory() as dest_dir):

            rsts = src_files[:5]
            txts = src_files[5:8]
            abcs = src_files[8:]

            cache = []
            for src in txts:
                new_src = src + '.txt'
                os.rename(src, new_src)
                cache.append(new_src)
            txts = cache

            cache = []
            for src in abcs:
                new_src = src + '.abc'
                os.rename(src, new_src)
                cache.append(new_src)
            abcs = cache

            mlos = [RST_FLAG, r'.+\.rst', r'.+\.txt', EXPR_FLAG]

            result = run_recursive_mode(src_dir, dest_dir, *mlos)
            assert result.returncode == 0

            for src in rsts:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)

            for src in txts:
                rel = os.path.relpath(src, src_dir)
                filename, _ = os.path.splitext(rel)
                dest = os.path.join(dest_dir, filename + '.html')
                assert_succ_render(src, dest)
