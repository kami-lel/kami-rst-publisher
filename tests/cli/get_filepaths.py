"""
get file/directory paths of various testing raw source files
"""


from pathlib import Path
import shutil
import os


testees_dir = Path(__file__).parent.parent / 'testees'

rst_simple = (testees_dir / 'rst_simple.rst').resolve()
rst_comprehensive = (testees_dir / 'rst_comprehensive.rst').resolve()

rst_recursive1 = (testees_dir / 'rst_recursive1').resolve()
rst_recursive2 = (testees_dir / 'rst_recursive2').resolve()
rst_recursive3 = (testees_dir / 'rst_recursive3').resolve()


def _copy_basic_to(dest_dir):
    rst_simple_dest = (Path(dest_dir) / 'rst_simple.rst').resolve()
    shutil.copy2(rst_simple, rst_simple_dest)
    rst_comprehensive_dest = \
            (Path(dest_dir) / 'rst_comprehensive.rst').resolve()
    shutil.copy2(rst_comprehensive, rst_comprehensive_dest)


def copy_rst_recursive1_to(dest_dir):
    _copy_basic_to(dest_dir)
    shutil.copytree(rst_recursive1, dest_dir, dirs_exist_ok=True)
    os.chmod(dest_dir, 0o755)


def copy_rst_recursive2_to(dest_dir):
    _copy_basic_to(dest_dir)
    shutil.copytree(rst_recursive1, dest_dir, dirs_exist_ok=True)
    shutil.copytree(rst_recursive2, dest_dir, dirs_exist_ok=True)
    os.chmod(dest_dir, 0o755)


def copy_rst_recursive3_to(dest_dir):
    _copy_basic_to(dest_dir)
    shutil.copytree(rst_recursive1, dest_dir, dirs_exist_ok=True)
    shutil.copytree(rst_recursive2, dest_dir, dirs_exist_ok=True)
    shutil.copytree(rst_recursive3, dest_dir, dirs_exist_ok=True)
    os.chmod(dest_dir, 0o755)

