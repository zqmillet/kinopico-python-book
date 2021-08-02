import os
import pytest

from extensions.tikz import code_to_svg

@pytest.fixture
def code():
    return r"""
    \documentclass[a4paper,10pt]{article}
    \usepackage{tikz}
    \usepackage{verbatim}
    \usepackage[active,tightpage]{preview}
    \PreviewEnvironment{tikzpicture}
    \setlength\PreviewBorder{5pt}%
    \usetikzlibrary{arrows,chains,matrix,positioning,scopes}
    \makeatletter
    \tikzset{join/.code=\tikzset{after node path={%
    \ifx\tikzchainprevious\pgfutil@empty\else(\tikzchainprevious)%
    edge[every join]#1(\tikzchaincurrent)\fi}}}
    \makeatother
    %
    \tikzset{>=stealth',every on chain/.append style={join},
             every join/.style={->}}
    \tikzstyle{labeled}=[execute at begin node=$\scriptstyle,
       execute at end node=$]
    %
    \begin{document}
    \begin{tikzpicture}
      \matrix (m) [matrix of math nodes, row sep=3em, column sep=3em]
        { 0 & A  & B  & C  & 0 \\
          0 & A' & B' & C' & 0 \\ };
      { [start chain] \chainin (m-1-1);
        \chainin (m-1-2);
        { [start branch=A] \chainin (m-2-2)
            [join={node[right,labeled] {\eta_1}}];}
        \chainin (m-1-3) [join={node[above,labeled] {\varphi}}];
        { [start branch=B] \chainin (m-2-3)
            [join={node[right,labeled] {\eta_2}}];}
        \chainin (m-1-4) [join={node[above,labeled] {\psi}}];
        { [start branch=C] \chainin (m-2-4)
            [join={node[right,labeled] {\eta_3}}];}
        \chainin (m-1-5); }
      { [start chain] \chainin (m-2-1);
        \chainin (m-2-2);
        \chainin (m-2-3) [join={node[above,labeled] {\varphi'}}];
        \chainin (m-2-4) [join={node[above,labeled] {\psi'}}];
        \chainin (m-2-5); }
    \end{tikzpicture}
    \end{document}
    """

@pytest.fixture
def file_path():
    path = 'main.svg'
    yield path
    os.remove(path)

def test_code_to_pdf(code, file_path):
    code_to_svg(code, file_path) 
    assert os.path.isfile(file_path)
