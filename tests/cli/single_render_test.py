"""
test single mode of cli
"""


import tempfile
import re

from cli_test_shared import rst_simple, rst_comprehensive, \
        run_single_mode, assert_succ_rst_render


class TestRender:

    def test_rst1(_):  # use rst_simple
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            src = rst_simple
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert_succ_rst_render(src, dest)

    def test_rst2(_):  # use rst_comprehensive
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            src = rst_comprehensive
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0

            assert_succ_rst_render(src, dest)
