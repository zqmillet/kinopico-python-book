import sys
from sys import executable
from dis import dis
from io import StringIO
from docutils.parsers.rst.directives.misc import Raw
from docutils.parsers.rst import directives
from ansi2html import Ansi2HTMLConverter
from contextlib import contextmanager
from colorama import Style, Fore
from pexpect import spawn
from textwrap import dedent
from sphinx.directives.code import CodeBlock
from docutils.statemachine import StringList

def get_interactive_result(code):
    child = spawn(executable, encoding='utf8')
    for line in code.strip().splitlines():
        child.sendline(line)

    output = child.read().replace('\r', '')
    return output.replace('\n' + code, '').strip()

class Bash(Raw):
    has_content = True
    required_arguments = 0

    option_spec = {
        'norun': directives.flag,
        'real_cmd': directives.unchanged,
    }

    variables = {
        'python': executable
    }

    def run(self):
        self.arguments[:] = ['html']

        norun = 'norun' in self.options
        display_command = '\n'.join(self.content).format(**self.variables).strip()
        real_command = (self.options.get('real_cmd') or display_command).format(**self.variables)
        convertor = Ansi2HTMLConverter(dark_bg=True)

        if not norun:
            output = spawn(real_command, env={'TERM': 'screen', 'COLORTERM': 'truecolor', 'COLORFGBG': '7;0'}).read()
            html = convertor.convert(f'{Style.BRIGHT}{Fore.RED}${Fore.BLACK} {display_command}{Fore.RESET}{Style.RESET_ALL}\n{output.decode("utf8").strip()}')
        else:
            html = convertor.convert(f'{Style.BRIGHT}{Fore.RED}${Fore.BLACK} {display_command}{Fore.RESET}{Style.RESET_ALL}')

        self.content[0] = f'<div class="highlight", style="background-color:#F8F8F8;">{html}</div>'
        return super().run()

class Python(Raw):
    has_content = True
    required_arguments = 0

    def run(self):
        self.arguments[:] = ['html']

        display_command = 'python ' + '\n'.join(self.content).strip()
        real_command = executable + ' ' + '\n'.join(self.content).strip()
        convertor = Ansi2HTMLConverter(dark_bg=True)

        output = spawn(real_command, env={'TERM': 'screen', 'COLORTERM': 'truecolor', 'COLORFGBG': '7;0'}).read()
        html = convertor.convert(f'{Style.BRIGHT}{Fore.RED}${Fore.BLACK} {display_command}{Fore.RESET}{Style.RESET_ALL}\n{output.decode("utf8").strip()}')

        self.content[0] = f'<div class="highlight", style="background-color:#F8F8F8;">{html}</div>'
        return super().run()

@contextmanager
def stdout():
    string = StringIO()
    origin_stdout = sys.stdout
    sys.stdout = string
    yield string
    sys.stdout = origin_stdout

class Dis(CodeBlock):
    has_content = True
    required_arguments = 0

    def run(self):
        file_path = self.arguments[0]
        with open(file_path, 'r', encoding='utf8') as file:
            code = file.read()

        with stdout() as string:
            dis(code)

        self.arguments[:] = ['text']
        self.content = StringList(dedent(string.getvalue()).splitlines())
        self.options['caption'] = f':py:obj:`{file_path}` 字节码的反汇编'
        return super().run()

class Interpreter(Raw):
    has_content = True
    required_arguments = 0

    def run(self):
        self.arguments[:] = ['html']

        display_command = 'python'
        convertor = Ansi2HTMLConverter(dark_bg=True)

        code = '\n'.join(self.content).strip()
        output = get_interactive_result(code)
        html = convertor.convert(f'{Style.BRIGHT}{Fore.RED}${Fore.BLACK} {display_command}{Fore.RESET}{Style.RESET_ALL}\n{output}')

        self.content[0] = f'<div class="highlight", style="background-color:#F8F8F8;">{html}</div>'
        self.content[:] = self.content[:1]
        return super().run()

def setup(app):
    app.add_directive('bash', Bash)
    app.add_directive('python', Python)
    app.add_directive('interpreter', Interpreter)
    app.add_directive('dis', Dis)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
