import os

author = 'kinopico'
project = 'kinopico\'s python book'

extensions = [
    'extensions.codeblock',
    'sphinxcontrib.tikz',
    'sphinx.ext.graphviz',
]

html_theme = 'sphinx_rtd_theme'
html_favicon = './static/kinopico.png'
html_codeblock_linenos_style = 'table'

graphviz_output_format = 'svg'
graphviz_dot_args = ['-Nfontsize=10', '-Efontsize=10', '-Kneato']
source_suffix = ['.rst']

numfig = True
numfig_format = {
    'code-block': '代码 %s',
    'section': '章节 %s'
}

rst_prolog = '''
.. role:: py(code)
   :language: py
   :class: highlight

.. role:: sh(code)
   :language: console
   :class: highlight
'''

tikz_latex_preamble = r'''
\usepackage{{ctex}}
\setmainfont[Path={current_directory}/fonts/pingfang/, UprightFont=*_regular, BoldFont=*_bold]{{pingfang}}
\setCJKmainfont[Path={current_directory}/fonts/pingfang/, UprightFont=*_regular, BoldFont=*_bold]{{pingfang}}
\setmonofont[Path={current_directory}/fonts/sfmono/, UprightFont=*_regular, BoldFont=*_bold]{{sfmono}}
'''.format(current_directory=os.path.abspath(os.curdir))

tikz_latex_preamble += r'''
\tikzset{
    reference/.style = {draw=black, rectangle, line width=1pt, minimum width=0.9cm, minimum height=0.9cm, font=\tt},
    object/.style = {fill=green!40!black, rectangle, line width=1pt, minimum width=0.9cm, minimum height=0.9cm, font=\tt, text=white},
    code/.style = {font=\tt, anchor=west},
    ref/.style = {line width=1pt, ->}
}
'''

tikz_tikzlibraries='positioning'

latex_engine = 'xelatex'
