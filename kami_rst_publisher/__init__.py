
from docutils.parsers.rst.roles import register_local_role
from docutils.parsers.rst.directives import register_directive

from .role import smart_role, tag_role
from .directive import TagDirective, SubtitleDirective
from .rst2html_file import Rst2htmlFile, Rst2htmlFileBatch, Rst2htmlFileRecursive


def init_publisher():
    # register local roles
    register_local_role("smart", smart_role)
    register_local_role("tag", tag_role)

    # register directives
    register_directive("tag", TagDirective)
    register_directive("subtitle", SubtitleDirective)
