"""
test recursive mode of cli
"""


import tempfile
import os
import re


from cli_test_shared import  run_recursive_mode, assert_succ_rst_render, \
        copy_rst_recursive1_to, copy_rst_recursive2_to, copy_rst_recursive3_to


def _find_subfiles_recursively(root):
    entries = []
    for dirpath, _, filesnames in os.walk(root):
        for filename in filesnames:
            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, root)
            entry = (full_path, rel_path)
            entries.append(entry)
    return entries


class TestRender:  #  yes DESTINATION, no suffix

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            copy_rst_recursive1_to(src_dir)

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            src_entries = _find_subfiles_recursively(src_dir)
            dest_entries = _find_subfiles_recursively(dest_dir)

            assert len(src_entries) == len(dest_entries)
            for (src, _), (dest, _) in zip(src_entries, dest_entries):
                assert_succ_rst_render(src, dest)

    def test2(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            copy_rst_recursive1_to(src_dir)

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            src_entries = _find_subfiles_recursively(src_dir)
            dest_entries = _find_subfiles_recursively(dest_dir)

            assert len(src_entries) == len(dest_entries)
            for (src, _), (dest, _) in zip(src_entries, dest_entries):
                assert_succ_rst_render(src, dest)

    def test3(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            copy_rst_recursive2_to(src_dir)

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            src_entries = _find_subfiles_recursively(src_dir)
            dest_entries = _find_subfiles_recursively(dest_dir)

            assert len(src_entries) == len(dest_entries)
            for (src, _), (dest, _) in zip(src_entries, dest_entries):
                assert_succ_rst_render(src, dest)


class TestAlongside:  #  no DESTINATION

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
                    assert_succ_rst_render(full_path, dest)
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
                    assert_succ_rst_render(full_path, dest)
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
                    assert_succ_rst_render(full_path, dest)
                    cnt += 1

            assert len(entries) == cnt * 2


class TestEmptySrc:  # warning is logged when nothing published

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            assert re.search('WARNING nothing published', result.stdout)
