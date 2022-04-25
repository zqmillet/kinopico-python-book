import os

author = 'kinopico'
project = 'kinopico\'s python book'

extensions = [
    'extensions.codeblock',
    'extensions.bash',
    'sphinxcontrib.tikz',
    'sphinx.ext.graphviz',
]

html_theme = 'sphinx_rtd_theme'
html_favicon = './_static/kinopico.png'
html_codeblock_linenos_style = 'table'

graphviz_output_format = 'svg'
graphviz_dot_args = ['-Nfontsize=10', '-Efontsize=10', '-Kneato']
source_suffix = ['.rst']

html_static_path = ['_static']

html_css_files = ['style.css']

numfig = True
numfig_format = {
    'code-block': '代码 %s',
    'figure': '图 %s',
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
\definecolor{reference}{rgb}{0.63, 0.79, 0.95}
\definecolor{object}{rgb}{0.66, 0.89, 0.63}
\tikzset{
    reference/.style = {fill=reference, rectangle, line width=1pt, minimum width=0.9cm, minimum height=0.9cm, font=\tt\footnotesize},
    object/.style = {fill=object, rectangle, line width=1pt, minimum width=0.9cm, minimum height=0.9cm, font=\tt\footnotesize},
    code/.style = {font=\tt\footnotesize, anchor=west},
    plaintext/.style = {font=\footnotesize\bf, anchor=base},
    ref/.style = {line width=1pt, ->}
}
'''

tikz_tikzlibraries='positioning'

latex_engine = 'xelatex'
