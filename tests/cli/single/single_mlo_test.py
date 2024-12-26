"""
MLO errors in single mode

essentially test of MLOConfigSingleWebServerMode
"""


import re

from ... import TesteeDir
from .. import run_single_mode, MD_FLAG, RST_FLAG, EXPR_FLAG


class TestTooMany:  # too many MLO

    def test_single1(_):  # single mode
        with (TesteeDir('rst_simple') as (_, src_files)):
            result = run_single_mode(src_files[0], MD_FLAG, RST_FLAG)

            assert result.returncode == 22
            assert re.search(
                    ('CRITICAL more than 1 markup langauge option is given '
                    'in single/web server mode'), result.stderr)

    def test_web1(_):  # web mode
        with (TesteeDir('rst_simple') as (_, src_files)):
            result = run_single_mode(src_files[0], MD_FLAG, RST_FLAG, '-w')

            assert result.returncode == 22
            assert re.search(
                    ('CRITICAL more than 1 markup langauge option is given '
                    'in single/web server mode'), result.stderr)


class TestNoFilterSingle:  #  single/web mode does not allow giving filter

    def test_single_ext1(_):
        with (TesteeDir('rst_simple') as (_, src_files)):
            src = src_files[0]
            ext = 'txt'

            result = run_single_mode(src, MD_FLAG, ext)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL single/web server mode not allow any FILTER: ',
                    result.stderr)

    def test_single_ext2(_):
        with (TesteeDir('rst_simple') as (_, src_files)):
            src = src_files[0]
            ext = 'txt'

            result = run_single_mode(src, RST_FLAG, ext)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL single/web server mode not allow any FILTER: ',
                    result.stderr)

    def test_single_ext3(_):
        with (TesteeDir('rst_simple') as (_, src_files)):
            src = src_files[0]
            ext = 'txt'
            ext2 = 'def'

            result = run_single_mode(src, RST_FLAG, ext, ext2)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL single/web server mode not allow any FILTER: ',
                    result.stderr)

    def test_single_regex1(_):
        with (TesteeDir('rst_simple') as (_, src_files)):
            src = src_files[0]
            regex = r'.+\.rst'

            result = run_single_mode(src, MD_FLAG, regex, EXPR_FLAG)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL single/web server mode not allow any FILTER: ',
                    result.stderr)
