
from docutils.nodes import literal, strong, raw


def smart_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    first = text[0]

    if text[0:3] == 'KS.' or text == 'KS':
        # KScode
        html_text = r'<span class="kami-KScode">{}</span>'.format(text)
        nodes = [raw(rawtext, html_text, format='html')]
    elif first == '.':
        # KSproxy
        p_node = raw('p', r'<span class="kami-KSsup">p</span>', format='html')
        text_node = raw(rawtext, r'<span class="kami-KSproxy">{}</span>'.format(text), format='html')
        nodes = [p_node, text_node]
    elif first.isnumeric():
        # Arabic number
        html_text = r'<span class="kami-ArabicNumber">{}</span>'.format(text)
        nodes = [raw(rawtext, html_text, format='html')]
    elif first.lower() in 'oivxl':
        # Roman numeral
        html_text = r'<span class="kami-RomanNumeral">{}</span>'.format(text)
        nodes = [raw(rawtext, html_text, format='html')]
    else:
        # fallback
        nodes = [strong(rawtext, text)]

    return nodes, []


def tag_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    t_node = raw('t', r'<span class="kami-KSsup">T</span>', format='html')
    text_node = literal(rawtext, text)
    nodes = [t_node, text_node]
    return nodes, []
