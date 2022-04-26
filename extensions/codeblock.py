import sys
import subprocess
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList
from sphinx.directives.code import LiteralInclude
from sphinx.directives.code import CodeBlock

class CodeFile(LiteralInclude):
    def run(self):
        file_path, *_ = self.arguments
        self.arguments[:] = ['/' + file_path]
        self.options['caption'] = f':py:obj:`{file_path.strip("/")}`'
        self.options['linenos'] = True
        return super().run()

def setup(app):
    app.add_directive("code_file", CodeFile)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
