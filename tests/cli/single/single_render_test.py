"""
test single mode of cli
"""


import tempfile
import re

from .. import rst_simple, rst_comprehensive, \
        run_single_mode, assert_succ_rst_render


class TestRender:

    def test_rst1(_):  # use rst_simple
        with tempfile.NamedTemporaryFile() as temp_file:
            src = rst_simple
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0
            assert_succ_rst_render(src, dest)

    def test_rst2(_):  # use rst_comprehensive
        with tempfile.NamedTemporaryFile() as temp_file:
            src = rst_comprehensive
            dest = temp_file.name

            result = run_single_mode(src, dest)
            assert result.returncode == 0

            assert_succ_rst_render(src, dest)


class TestErrMLO:  # test related to markup langauge options

    def test_too_many1(_): # too many MLO
        src = rst_simple

        result = run_single_mode(src, '--md', '--rst')
        assert result.returncode == 22
        assert re.search(
                ('CRITICAL more than 1 markup langauge option is given '
                'in single/web server mode'), result.stderr)

    def test_bad_filter1(_):  # filter is illegal pattern
        src = rst_simple
        bad_pattern = r'[abc'

        result = run_single_mode(src, '--md', bad_pattern)
        assert result.returncode == 22
        assert re.search('CRITICAL option --md gets an illegal regex pattern:',
                result.stderr)




