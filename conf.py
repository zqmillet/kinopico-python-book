author = 'kinopico'
project = 'kinopico\'s python book'

extensions = [
    'extensions.codeblock',
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

