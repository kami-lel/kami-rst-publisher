"""
test single mode of cli rendering md
"""


import tempfile
from .. import MD_FLAG, \
        md_simple, md_comprehensive, \
        run_single_mode, assert_succ_render


class TestRenderMLO:  # with --md

    def test1(_):  # use rst_simple
        with tempfile.NamedTemporaryFile() as temp_file:
            src = md_simple
            dest = temp_file.name

            result = run_single_mode(src, dest, MD_FLAG)
            assert result.returncode == 0
            assert_succ_render(src, dest)
