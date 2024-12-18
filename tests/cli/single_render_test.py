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


class TestRender:

    def test_rst1(_):  # use rst_simple
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            src = rst_simple
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0

            # assert each line in source file is present in output
            with (open(src, 'r') as ipt_file, open(dest, 'r') as dest_file):
                dest_read = dest_file.read()
                for line in ipt_file:
                    if line.isalpha():
                        assert line in dest_read


    def test_rst2(_):  # use rst_comprehensive
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            src = rst_comprehensive
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0

            # assert each line in source file is present in output
            with (open(src, 'r') as ipt_file, open(dest, 'r') as dest_file):
                dest_read = dest_file.read()
                for line in ipt_file:
                    if line.isalpha():
                        assert line in dest_read
