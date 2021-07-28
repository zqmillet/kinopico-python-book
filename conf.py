author = 'kinopico'
project = 'kinopico\'s python book'

html_theme = 'sphinx_rtd_theme'
extensions = ['extensions.codeblock']

source_suffix = ['.rst']
html_codeblock_linenos_style = 'table'

rst_prolog = '''
.. role:: py(code)
   :language: py
   :class: highlight
'''

