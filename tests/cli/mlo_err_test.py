"""
errors related with MLO
"""


import re

from . import rst_simple, run_single_mode, run_recursive_mode, EXPR_FLAG


class TestTooMany:  # too many MLO

    def test_single1(_):  # single mode
        src = rst_simple

        result = run_single_mode(src, '--md', '--rst')
        assert result.returncode == 22
        assert re.search(
                ('CRITICAL more than 1 markup langauge option is given '
                'in single/web server mode'), result.stderr)

    def test_web1(_):
        src = rst_simple

        result = run_single_mode(src, '--web-server', '--md', '--rst')
        assert result.returncode == 22
        assert re.search(
                ('CRITICAL more than 1 markup langauge option is given '
                'in single/web server mode'), result.stderr)


class TestNoFilter:  #  single/web mode does not allow giving filter

    def test_single_ext1(_):
        src = rst_simple
        ext = 'txt'

        result = run_single_mode(src, '--md', ext)
        assert result.returncode == 22
        assert re.search(
                'CRITICAL single/web server mode not allow any FILTER: ',
                result.stderr)

    def test_single_ext2(_):
        src = rst_simple
        ext = 'txt'

        result = run_single_mode(src, '--rst', ext)
        assert result.returncode == 22
        assert re.search(
                'CRITICAL single/web server mode not allow any FILTER: ',
                result.stderr)

    def test_single_ext3(_):
        src = rst_simple
        ext = 'txt'
        ext2 = 'def'

        result = run_single_mode(src, '--rst', ext, ext2)
        assert result.returncode == 22
        assert re.search(
                'CRITICAL single/web server mode not allow any FILTER: ',
                result.stderr)

    def test_single_regex1(_):
        src = rst_simple
        regex = r'.+\.rst'

        result = run_single_mode(src, '--md', regex, EXPR_FLAG)
        assert result.returncode == 22
        assert re.search(
                'CRITICAL single/web server mode not allow any FILTER: ',
                result.stderr)

    def test_web_ext1(_):
        src = rst_simple
        ext = 'txt'

        result = run_single_mode(src, '--md', ext)
        assert result.returncode == 22
        assert re.search(
                'CRITICAL single/web server mode not allow any FILTER: ',
                result.stderr)

    def test_web_regex1(_):
        src = rst_simple
        ext = 'txt'

        result = run_single_mode(src, '--md', ext, EXPR_FLAG)
        assert result.returncode == 22
        assert re.search(
                'CRITICAL single/web server mode not allow any FILTER: ',
                result.stderr)


class TestBadPatten:  # bad extension/regex legality in recursive mode

    def test_ext1(_):  # bad extension
        src = rst_simple
        bad_ext = '???'

        result = run_recursive_mode(src, '--md', bad_ext)
        assert result.returncode == 22
        assert re.search('CRITICAL option --md gets an illegal extension:',
                result.stderr)

    def test_ext2(_):
        src = rst_simple
        bad_ext = ''

        result = run_recursive_mode(src, '--md', bad_ext)
        assert result.returncode == 22
        assert re.search('CRITICAL option --md gets an illegal extension:',
               result.stderr)

    def test_ext3(_):
        src = rst_simple
        bad_ext = '.abc'

        result = run_recursive_mode(src, '--rst', bad_ext)
        assert result.returncode == 22
        assert re.search('CRITICAL option --rst gets an illegal extension:',
                result.stderr)

    def test_ext4(_):
        src = rst_simple
        bad_ext = '123?456'

        result = run_recursive_mode(src, '--md', bad_ext)
        assert result.returncode == 22
        assert re.search('CRITICAL option --md gets an illegal extension:',
                result.stderr)

    def test_ext5(_):
        src = rst_simple
        good_ext1 = 'rst'
        good_ext2 = 'txt'
        good_ext3 = 'md'
        bad_ext = '???'

        result = run_recursive_mode(src, 
                '--rst', good_ext1, good_ext2, '--md', good_ext3, bad_ext)
        assert result.returncode == 22
        assert re.search('CRITICAL option --md gets an illegal extension:',
                result.stderr)

    def test_regex1(_):  # bad regex expression
        src = rst_simple
        bad_pattern = r'[abc'

        result = run_recursive_mode(src, EXPR_FLAG,
                '--md', bad_pattern)
        assert result.returncode == 22
        assert re.search('CRITICAL option --md gets an illegal regex pattern:',
                result.stderr)

    def test_regex2(_):
        src = rst_simple
        good_pattern1 = r'.+\.rst'
        good_pattern2 = r'.+\.txt'
        bad_pattern = r'[abc'

        result = run_recursive_mode(src, EXPR_FLAG,
                '--md', good_pattern1, good_pattern2, bad_pattern)
        assert result.returncode == 22
        assert re.search('CRITICAL option --md gets an illegal regex pattern:',
                result.stderr)

    def test_regex3(_):
        src = rst_simple
        good_pattern1 = r'.+\.rst'
        good_pattern2 = r'.+\.txt'
        good_pattern3 = r'.+\.md'
        bad_pattern = r'[abc'

        result = run_recursive_mode(src, EXPR_FLAG,
                '--rst', good_pattern1, good_pattern2,
                '--md', good_pattern3, bad_pattern)
        assert result.returncode == 22
        assert re.search('CRITICAL option --md gets an illegal regex pattern:',
                result.stderr)

