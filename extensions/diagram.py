import re
import os
import sys
import subprocess
from docutils import nodes
from sphinx.util.nodes import set_source_info
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList
from sphinx.directives.code import LiteralInclude
from sphinx.directives.code import CodeBlock 
from sphinx.util.docutils import SphinxDirective
from docutils import nodes

class graphviz(nodes.General, nodes.Inline, nodes.Element):
    pass

def get_new_file_path(directory):
    files = os.listdir(directory)

    if not files:
        index = 1
    else:
        *_, file_name = sorted(files)
        match = re.match('diagram_(?P<index>\d+)\.svg', file_name)
        index = int(match.groupdict()['index'])

    return os.path.join(directory, 'diagram_' + str(index + 1).zfill(4) + '.svg')

def figure_wrapper(directive: Directive, node: graphviz, caption: str) -> nodes.figure:
    figure_node = nodes.figure('', node)
    if 'align' in node:
        figure_node['align'] = node.attributes.pop('align')

    inodes, messages = directive.state.inline_text(caption, directive.lineno)
    caption_node = nodes.caption(caption, '', *inodes)
    caption_node.extend(messages)
    set_source_info(directive, caption_node)
    figure_node += caption_node
    return figure_node


def get_svg_file(content, file_path='diagrams_image.svg', directory='diagrams'):
    exec('\n'.join(content))

    assert os.path.isfile(file_path)
    if not os.path.isdir(directory):
        os.makedirs(directory)

    new_file_path = get_new_file_path(directory)
    os.rename(file_path, new_file_path)
    return new_file_path

class Diagram(SphinxDirective):
    has_content = True

    def run(self):
        file_path = get_svg_file(self.content)
        node = graphviz()
        node['code'] = '\n'.join(self.content)
        node['file_name'] = file_path
        node['options'] = {'docname': file_path}
        import pdb; pdb.set_trace()
        figure = figure_wrapper(self, node, '2333')
        return [figure]

def setup(app):
    app.add_directive("diagram", Diagram)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
