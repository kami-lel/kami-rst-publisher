
from docutils.parsers.rst.roles import register_local_role
from docutils.parsers.rst.directives import register_directive

from .role import *
from .directive import *


# initialize publisher by importing this module

# register local roles
register_local_role("smart", smart_role)
register_local_role("tag", tag_role)

# register directives
register_directive("tag", TagDirective)
register_directive("subtitle", SubtitleDirective)
