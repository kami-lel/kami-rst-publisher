"""
test using --expression in --recursive FILTER
"""


EXPR_FLAG = '--expression'
TXT_FILTER = r'.+\.txt'


import tempfile
import re
import shutil
import os


from .. import VERBOSE_FLAG, SUFFIX_FLAG, run_recursive_mode, \
        copy_rst_basic_to, copy_rst_recursive1_to, txt_folder


def change_all_files_extension(dest_dir, new_extension):
    for filename in os.listdir(dest_dir):
        file_path = os.path.join(dest_dir, filename)
        if os.path.isfile(file_path):
            base, _ = os.path.splitext(filename)
            new_file_path = os.path.join(dest_dir, f"{base}.{new_extension}")
            os.rename(file_path, new_file_path)


class TestBadFilter:  # given filter is not a legal regex expression

    def test1(_):
        src_dir = '???'
        filter = r'[a-z'  # illegal
        result = run_recursive_mode(src_dir, EXPR_FLAG, filter)

        assert result.returncode == 22
        assert re.search(r'CRITICAL re .+ of FILTER: illegal regex pattern',
                result.stderr)


class TestSkipInfo:
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

