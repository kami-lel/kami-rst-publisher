"""
test recursive mode of cli
"""


import tempfile
import re


from .. import run_recursive_mode


class TestEmptySrc:  # warning is logged when nothing published

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

            assert re.search('WARNING nothing published', result.stdout)



class TestAppendVersion:

    def test1(_):  # TODO rst & md
        pass
        # test publisher version contained in file
        with open(dest, 'r') as f:
            assert re.search(
                    r'<!-- PUBLISHED BY kami_rst_publisher\.\#.+ -->',
                    f.read())
