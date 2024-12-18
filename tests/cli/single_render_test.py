"""
test single mode of cli
"""

import tempfile
from pathlib import Path
from sys import executable
import subprocess

from get_filepaths import rst_simple, rst_comprehensive


def run_single_mode(*args):
    opt_args = [executable, '-m', 'kami_rst_publisher']
    opt_args.extend(args)
    return subprocess.run(opt_args, capture_output=True, text=True)


def assert_good_rst_render(src_path, dest_path):
    # assert each line in source file is present in output
    with (open(src_path, 'r') as ipt_file, open(dest_path, 'r') as dest_file):
        dest_read = dest_file.read()
        for line in ipt_file:
            if line.isalpha():
                assert line in dest_read


class TestRender:

    def test_rst1(_):  # use rst_simple
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            src = rst_simple
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert_good_rst_render(src, dest)



    def test_rst2(_):  # use rst_comprehensive
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            src = rst_comprehensive
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0

            assert_good_rst_render(src, dest)