import sys
import subprocess
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList
from sphinx.directives.code import LiteralInclude
from sphinx.directives.code import CodeBlock

class IncludeCodeFile(LiteralInclude):
    def run(self):
        file_path, *_ = self.arguments
        self.arguments[:] = ['/' + file_path]
        self.options['caption'] = f':py:obj:`{file_path.strip("/")}`'
        self.options['linenos'] = True
        return super().run()

class OutputOfCode(CodeBlock):
    def run(self):
        self.content = StringList([''])
        file_path, *_ = self.arguments
        file_path = file_path.strip('/')
        cmd = [sys.executable, file_path]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = process.communicate()

        self.arguments = ['console']
        self.options['caption'] = f'output of ``{file_path}``'
        self.content[0] = f'''$ python3 {file_path}\n{output.decode('utf8')}'''
        return super().run()

def setup(app):
    app.add_directive("include_code_file", IncludeCodeFile)
    app.add_directive("output_of_code", OutputOfCode)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
