

import tempfile
import os
import re


from .. import  RST_FLAG, EXPR_FLAG, \
        run_recursive_mode, assert_succ_render, find_subfiles_recursively, \
        copy_rst_basic_to, \
        copy_rst_recursive1_to, copy_rst_recursive2_to, copy_rst_recursive3_to


class TestFilterExtension:  # given --rst fitlers as extension

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):
            copy_rst_basic_to(src_dir)

            rst_mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *rst_mlos)
            assert result.returncode == 0

            src_entries = find_subfiles_recursively(src_dir)
            dest_entries = find_subfiles_recursively(dest_dir)
            assert len(src_entries) == len(dest_entries)

            for (src, _), (dest, _) in zip(src_entries, dest_entries):
                assert_succ_render(src, dest)

    def test2(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):
            copy_rst_recursive1_to(src_dir)

            rst_mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *rst_mlos)
            assert result.returncode == 0

            src_entries = find_subfiles_recursively(src_dir)
            dest_entries = find_subfiles_recursively(dest_dir)
            assert len(src_entries) == len(dest_entries)

            for (src, _), (dest, _) in zip(src_entries, dest_entries):
                assert_succ_render(src, dest)

    def test3(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):
            copy_rst_recursive2_to(src_dir)

            rst_mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *rst_mlos)
            assert result.returncode == 0

            src_entries = find_subfiles_recursively(src_dir)
            dest_entries = find_subfiles_recursively(dest_dir)
            assert len(src_entries) == len(dest_entries)

            for (src, _), (dest, _) in zip(src_entries, dest_entries):
                assert_succ_render(src, dest)

    def test4(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):
            copy_rst_recursive3_to(src_dir)

            rst_mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *rst_mlos)
            assert result.returncode == 0

            src_entries = find_subfiles_recursively(src_dir)
            dest_entries = find_subfiles_recursively(dest_dir)
            assert len(src_entries) == len(dest_entries)

            for (src, _), (dest, _) in zip(src_entries, dest_entries):
                assert_succ_render(src, dest)

    def test_mix1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):
            copy_rst_recursive3_to(src_dir)

            rst_mlos = [RST_FLAG, 'rst']

            result = run_recursive_mode(src_dir, dest_dir, *rst_mlos)
            assert result.returncode == 0

            src_entries = find_subfiles_recursively(src_dir)
            dest_entries = find_subfiles_recursively(dest_dir)
            assert len(src_entries) == len(dest_entries)

            for (src, _), (dest, _) in zip(src_entries, dest_entries):
                assert_succ_render(src, dest)




class TestFilterRegex:  # given --rst fitlers as regex (i.e. -e)

    pass


# FIXME
class OTestAlongside:  #  no DESTINATION

    def test1(_):
        with (tempfile.TemporaryDirectory() as root):
            copy_rst_recursive1_to(root)
            result = run_recursive_mode(root)
            assert result.returncode == 0

            entries = _find_subfiles_recursively(root)
            cnt = 0
            for full_path, _ in entries:
                filename, extension = os.path.splitext(full_path)
                if extension == '.rst':
                    dest = filename + '.html'
                    assert os.path.isfile(dest)
                    assert_succ_render(full_path, dest)
                    cnt += 1

            assert len(entries) == cnt * 2

    def test2(_):
        with (tempfile.TemporaryDirectory() as root):
            copy_rst_recursive2_to(root)
            result = run_recursive_mode(root)
            assert result.returncode == 0

            entries = _find_subfiles_recursively(root)
            cnt = 0
            for full_path, _ in entries:
                filename, extension = os.path.splitext(full_path)
                if extension == '.rst':
                    dest = filename + '.html'
                    assert os.path.isfile(dest)
                    assert_succ_render(full_path, dest)
                    cnt += 1

            assert len(entries) == cnt * 2

    def test3(_):
        with (tempfile.TemporaryDirectory() as root):
            copy_rst_recursive3_to(root)
            result = run_recursive_mode(root)
            assert result.returncode == 0

            entries = _find_subfiles_recursively(root)
            cnt = 0
            for full_path, _ in entries:
                filename, extension = os.path.splitext(full_path)
                if extension == '.rst':
                    dest = filename + '.html'
                    assert os.path.isfile(dest)
                    assert_succ_render(full_path, dest)
                    cnt += 1

            assert len(entries) == cnt * 2