"""
test recursive mode of cli
"""


import tempfile

from single_render_test import run_single_mode
from get_filepaths import \
        copy_rst_recursive1_to, copy_rst_recursive2_to, copy_rst_recursive3_to


def run_recursive_mode(*args):
    return run_single_mode('--recursive', *args)




class TestRender:  #  yes DESTINATION, no suffix

    def test1(_):
        with (tempfile.TemporaryDirectory() as src_dir,
                tempfile.TemporaryDirectory() as dest_dir):

            copy_rst_recursive1_to(src_dir)

            result = run_recursive_mode(src_dir, dest_dir)
            assert result.returncode == 0

    def test2(_):
        pass

    def test3(_):
        pass


class TestSuf:  #  yes DESTINATION, yes suffix
    pass  # TODO


class TestAlongside:  #  no DESTINATION, no suffix
    pass  # TODO


class TestAlongsideSuf:  #  no DESTINATION, yes suffix
    pass  # TODO

