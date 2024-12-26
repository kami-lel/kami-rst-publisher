"""
MLO errors in rcursive mode

essentially test of MLOConfigRecursiveMode
"""


import re
import os

from ... import TesteeDir
from .. import run_recursive_mode, EXPR_FLAG, MD_FLAG, RST_FLAG


class TestAtLeastOneFilter:  # at least 1 filter is needed for each MLO

    def test1(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            result = run_recursive_mode(src_root, MD_FLAG)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL option --md must have at least one filter',
                    result.stderr)

    def test2(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            result = run_recursive_mode(src_root, RST_FLAG)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL option --rst must have at least one filter',
                    result.stderr)

    def test3(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            result = run_recursive_mode(src_root, RST_FLAG, 'rst', MD_FLAG)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL option --md must have at least one filter',
                    result.stderr)


class TestIllegalExtension:  # given ext is illegal

    def test1(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            bad_ext = '???'

            result = run_recursive_mode(src_root, MD_FLAG, bad_ext)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL option --md gets an illegal extension:',
                    result.stderr)

    def test2(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            bad_ext = ''

            result = run_recursive_mode(src_root, MD_FLAG, bad_ext)
            assert result.returncode == 22
            assert re.search('CRITICAL option --md gets an illegal extension:',
                   result.stderr)

    def test3(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            bad_ext = '.txt'

            result = run_recursive_mode(src_root, MD_FLAG, bad_ext)
            assert result.returncode == 22
            assert re.search('CRITICAL option --md gets an illegal extension:',
                   result.stderr)

    def test4(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            bad_ext = '123?456'

            result = run_recursive_mode(src_root, MD_FLAG, bad_ext)
            assert result.returncode == 22
            assert re.search('CRITICAL option --md gets an illegal extension:',
                    result.stderr)

    def test5(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            good_ext1 = 'rst'
            good_ext2 = 'txt'
            good_ext3 = 'md'
            bad_ext = '???'

            result = run_recursive_mode(src_root, 
                    RST_FLAG, good_ext1, good_ext2, MD_FLAG, good_ext3, bad_ext)
            assert result.returncode == 22
            assert re.search('CRITICAL option --md gets an illegal extension:',
                    result.stderr)


class TestWarningExtension:  # given ext will give warning

    def test_case1(_):  # warning about weird casing
        with (TesteeDir('rst_simple') as (src_root, src_files)):
            ext = 'Rst'

            src = os.path.realpath(os.path.join(src_root, 'rst_simple' + ext))
            os.rename(src_files[0], src)

            result = run_recursive_mode(src_root, RST_FLAG, ext)
            assert result.returncode == 0
            assert re.search(
    "option --rst gets extension with upper case: 'Rst', converted to 'rst'",
            result.stdout)

    def test_case2(_):
        with (TesteeDir('rst_simple') as (src_root, src_files)):
            ext = 'RST'

            src = os.path.realpath(os.path.join(src_root, 'rst_simple' + ext))
            os.rename(src_files[0], src)

            result = run_recursive_mode(src_root, RST_FLAG, ext)
            assert result.returncode == 0
            assert re.search(
    "option --rst gets extension with upper case: 'RST', converted to 'rst'",
            result.stdout)



class TestIllegalRegex:  # bad regex expression

    def test_regex1(_):  
        with (TesteeDir('rst_simple') as (src_root, _)):
            bad_pattern = r'[abc'

            result = run_recursive_mode(src_root, EXPR_FLAG,
                    MD_FLAG, bad_pattern)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL option --md gets an illegal regex pattern:',
                    result.stderr)

    def test_regex2(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            good_pattern1 = r'.+\.rst'
            good_pattern2 = r'.+\.txt'
            bad_pattern = r'[abc'

            result = run_recursive_mode(src_root, EXPR_FLAG,
                    MD_FLAG, good_pattern1, good_pattern2, bad_pattern)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL option --md gets an illegal regex pattern:',
                    result.stderr)

    def test_regex3(_):
        with (TesteeDir('rst_simple') as (src_root, _)):
            good_pattern1 = r'.+\.rst'
            good_pattern2 = r'.+\.txt'
            good_pattern3 = r'.+\.md'
            bad_pattern = r'[abc'

            result = run_recursive_mode(src_root, EXPR_FLAG,
                    RST_FLAG, good_pattern1, good_pattern2,
                    MD_FLAG, good_pattern3, bad_pattern)
            assert result.returncode == 22
            assert re.search(
                    'CRITICAL option --md gets an illegal regex pattern:',
                    result.stderr)
