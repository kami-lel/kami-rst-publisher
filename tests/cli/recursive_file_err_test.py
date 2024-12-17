"""
test recursive mode of cli, file related err
"""


import tempfile
import os
import re

from recursive_render_test import run_recursive_mode


class TestRoot:

    def test_no_perm(_):  # no permission to root
        with tempfile.TemporaryDirectory() as temp_dir:
            # BUG

            os.chmod(temp_dir, 0o133)  # no read permission
            result = run_recursive_mode(temp_dir)
            assert result.returncode == 2
            assert re.match(r"CRITICAL: re .+ of SOURCE: Permission denied",
                    result.stderr)

    def test_no_exs(_):  # non exist
        pass

    def test_file(_):  # is a file
        pass