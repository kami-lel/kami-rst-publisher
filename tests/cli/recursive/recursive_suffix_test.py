"""
test recursive mode of cli related to option --suffix
"""


import tempfile
import os


from .. import SUFFIX_FLAG, \
        copy_rst_basic_to,  copy_rst_recursive3_to, \
        run_recursive_mode, assert_succ_render


class TestWithDest:  # with DESTINATION

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            copy_rst_basic_to(src_dir)

            suf = '_suf'
            result = run_recursive_mode(src_dir, dest_dir, SUFFIX_FLAG, suf)

            assert result.returncode == 0
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

    def test2(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            copy_rst_recursive3_to(src_dir)

            suf = '_suf'
            result = run_recursive_mode(src_dir, dest_dir, SUFFIX_FLAG, suf)

            assert result.returncode == 0
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

    def test_dft1(_):  # use default suffix
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            copy_rst_basic_to(src_dir)

            result = run_recursive_mode(src_dir, dest_dir, SUFFIX_FLAG)

            assert result.returncode == 0
            # check each file exists
            suf = '.R'
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
        with tempfile.TemporaryDirectory() as root:

            copy_rst_basic_to(root)

            suf = '_suf'
            result = run_recursive_mode(root, SUFFIX_FLAG, suf)

            assert result.returncode == 0
            # check each file exists
            for dir_name, _, files in os.walk(root):
                for full_filename in files:
                    src = os.path.join(dir_name, full_filename)
                    filename, extension = os.path.splitext(src)
                    if extension == '.rst':
                        dest = filename + suf + '.html'

                        assert os.path.isfile(dest)
                        assert_succ_render(src, dest)

    def test2(_):
        with tempfile.TemporaryDirectory() as root:

            copy_rst_recursive3_to(root)

            suf = '_suf'
            result = run_recursive_mode(root, SUFFIX_FLAG, suf)

            assert result.returncode == 0
            # check each file exists
            for dir_name, _, files in os.walk(root):
                for full_filename in files:
                    src = os.path.join(dir_name, full_filename)
                    filename, extension = os.path.splitext(src)
                    if extension == '.rst':
                        dest = filename + suf + '.html'

                        assert os.path.isfile(dest)
                        assert_succ_render(src, dest)


    def test_dft1(_):  # use default suffix
        with tempfile.TemporaryDirectory() as root:

            copy_rst_recursive3_to(root)

            result = run_recursive_mode(root, SUFFIX_FLAG)

            assert result.returncode == 0
            # check each file exists
            suf = '.R'
            for dir_name, _, files in os.walk(root):
                for full_filename in files:
                    src = os.path.join(dir_name, full_filename)
                    filename, extension = os.path.splitext(src)
                    if extension == '.rst':
                        dest = filename + suf + '.html'

                        assert os.path.isfile(dest)
                        assert_succ_render(src, dest)
