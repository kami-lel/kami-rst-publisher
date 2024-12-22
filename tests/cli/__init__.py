"""
get file/directory paths of various testing raw source files
"""


VERBOSE_FLAG = '--verbose'
SUFFIX_FLAG = '--suffix'
EXPR_FLAG = '-e'
RST_FLAG = '--rst'
MD_FLAG = '--md'


from pathlib import Path
import shutil
import os
from sys import executable
import subprocess
import re


testees_folder = Path(__file__).parent.parent / 'testees'
rst_folder = testees_folder / 'rst'

rst_simple = (rst_folder / 'rst_simple.rst').resolve()
rst_comprehensive = (rst_folder / 'rst_comprehensive.rst').resolve()

rst_recursive1 = (rst_folder / 'rst_recursive1').resolve()
rst_recursive2 = (rst_folder / 'rst_recursive2').resolve()
rst_recursive3 = (rst_folder / 'rst_recursive3').resolve()

txt_folder = (testees_folder / 'plain_text').resolve()

md_folder = testees_folder / 'md'

md_simple = (md_folder / 'md_simple.md').resolve()
md_comprehensive = (md_folder / 'md_comprehensive.md').resolve()




def run_single_mode(*args):
    opt_args = [executable, '-m', 'kami_rst_publisher']
    opt_args.extend(args)
    return subprocess.run(opt_args, capture_output=True, text=True)


def run_recursive_mode(*args):
    return run_single_mode('--recursive', *args)


def assert_succ_render(src_path, dest_path):
    # assert each line in source file is present in output
    with (open(src_path, 'r') as ipt_file, open(dest_path, 'r') as dest_file):
        dest_read = dest_file.read()
        for line in ipt_file:
            if line.isalnum():
                assert line in dest_read

        assert re.search(
                r'<!-- PUBLISHED BY kami_rst_publisher\.\#.+ -->', dest_read)


def copy_rst_basic_to(dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    rst_simple_dest = (Path(dest_dir) / 'rst_simple.rst').resolve()
    shutil.copy2(rst_simple, rst_simple_dest)
    rst_comprehensive_dest = \
            (Path(dest_dir) / 'rst_comprehensive.rst').resolve()
    shutil.copy2(rst_comprehensive, rst_comprehensive_dest)


def copy_rst_recursive1_to(dest_dir):
    copy_rst_basic_to(dest_dir)
    shutil.copytree(rst_recursive1, dest_dir, dirs_exist_ok=True)
    os.chmod(dest_dir, 0o755)


def copy_rst_recursive2_to(dest_dir):
    copy_rst_basic_to(dest_dir)
    shutil.copytree(rst_recursive1, dest_dir, dirs_exist_ok=True)
    shutil.copytree(rst_recursive2, dest_dir, dirs_exist_ok=True)
    os.chmod(dest_dir, 0o755)


def copy_rst_recursive3_to(dest_dir):
    copy_rst_basic_to(dest_dir)
    shutil.copytree(rst_recursive1, dest_dir, dirs_exist_ok=True)
    shutil.copytree(rst_recursive2, dest_dir, dirs_exist_ok=True)
    shutil.copytree(rst_recursive3, dest_dir, dirs_exist_ok=True)
    os.chmod(dest_dir, 0o755)
