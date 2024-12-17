"""
test recursive mode of cli
"""

import tempfile
from pathlib import Path
from sys import executable
import subprocess

from single_render_test import run_single_mode


def run_recursive_mode(*args):
    return run_single_mode('--recursive', *args)

