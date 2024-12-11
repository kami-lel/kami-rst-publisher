
from docutils.parsers.rst import Directive
from docutils.nodes import subtitle, literal_block, raw


__all__ = ('TagDirective', 'SubtitleDirective')


class TagDirective(Directive):

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    has_content = True

    def run(self):
        ks_tag_node = raw('KS.Tag', r'<span class="kami-KSTag">KS.Tag</span>', format='html')
        texts = '\n'.join(self.content)
        literal_node = literal_block(texts, texts)
        return [ks_tag_node, literal_node]


class SubtitleDirective(Directive):

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    has_content = True

    def run(self):
        subtitle_nodes = [subtitle(txt, txt) for txt in self.content]
        return subtitle_nodes
