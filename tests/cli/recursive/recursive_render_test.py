"""
test recursive mode of cli
"""


import tempfile
import re


from ... import TesteeDir
from .. import run_recursive_mode


class TestEmptySrc:  # warning is logged when nothing published

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            assert re.search('WARNING nothing published', result.stdout)


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



class OTestBadFilter:  # given filter is not a legal regex expression

    def test1(_):
        src_dir = '???'
        filter = r'[a-z'  # illegal
        result = run_recursive_mode(src_dir, EXPR_FLAG, filter)

        assert result.returncode == 22
        assert re.search(r'CRITICAL re .+ of FILTER: illegal regex pattern',
                result.stderr)


