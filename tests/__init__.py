

from pathlib import Path
import tempfile
import shutil
import os


testees_folder = Path(__file__).parent / 'testees'


class TesteeDir(object):

    DEPENDENCIES = {
'rst_recursive1': [
        'rst_simple', 'rst_comprehensive1', 'rst_comprehensive2'
        ], 
'rst_recursive2': [
        'rst_simple', 'rst_comprehensive1', 'rst_comprehensive2',
        'rst_recursive1'
        ], 
'rst_recursive3': [
        'rst_simple', 'rst_comprehensive1', 'rst_comprehensive2',
        'rst_recursive1', 'rst_recursive2'
        ], 
'mix': [
        'rst_simple', 'rst_comprehensive1', 'rst_comprehensive2',
        'rst_recursive1', 'rst_recursive2', 'rst_recursive3',
        'md_simple', 'md_comprehensive', 'md_extended',
        'txt'
        ], 
    }

    def __init__(self, *args):
        self.args = args

    def __enter__(self):
        self.dir = tempfile.TemporaryDirectory()
        self.dir_name = self.dir.name

        for arg in self.args:
            if arg in self.DEPENDENCIES:
                for key in self.DEPENDENCIES[arg]:
                    self.copy(key)

            self.copy(arg)

        # recursively change all files  premission
        os.chmod(self.dir_name, 0o755)

        file_paths = []
        for dirpath, _, filenames in os.walk(self.dir_name):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                file_paths.append(full_path)

        return self.dir_name, file_paths

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.dir.cleanup()

    def copy(self, key):
        testee_dir = (testees_folder / key).resolve()
        shutil.copytree(testee_dir, self.dir_name, dirs_exist_ok=True)
