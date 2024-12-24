
# TODO use TesteeDir

import tempfile
import os


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




class OTestSkipInfo:
    # test when files in src are skipped b/c not matching FILTER
    # it should log info

    def test_dft1(_):  # default filter for .rst
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            shutil.copytree(txt_folder, src_dir, dirs_exist_ok=True)
            os.chmod(src_dir, 0o755)

            result = run_recursive_mode(src_dir, dest_dir, VERBOSE_FLAG)

            assert result.returncode == 0
            assert len(re.findall(r'INFO skip file:', result.stdout)) == 2
            assert re.search('WARNING nothing published', result.stdout)

    def test1(_):  # customized suffix
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            copy_rst_basic_to(src_dir)
            change_all_files_extension(src_dir, 'txt')
            copy_rst_basic_to(src_dir)

            result = run_recursive_mode(src_dir, dest_dir,
                    EXPR_FLAG, TXT_FILTER, VERBOSE_FLAG)

            assert result.returncode == 0
            assert len(re.findall(r'INFO skip file: ', result.stdout)) == 2
            assert len(re.findall(r'INFO publish: ', result.stdout)) == 2

