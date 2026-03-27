# ==============================================================================
# assets/macros.py — Threat Surfaces | fischer³ Education
#
# Single source of truth for all course MathJax macro definitions.
# Mirrors assets/latex-preamble.tex exactly.
#
# Usage in every notebook (first code cell):
#
#   Local / JupyterLab / VS Code:
#       from assets.macros import inject
#       inject()
#
#   Google Colab (handled automatically by the standard setup cell —
#   see assets/notebook_setup.py):
#       import urllib.request
#       exec(urllib.request.urlopen(MACROS_URL).read().decode())
#       inject()
#
# When a macro changes, update this file only. All notebooks pick up
# the change automatically on next run.
# ==============================================================================

from IPython.display import display, Markdown

# ------------------------------------------------------------------------------
# Macro definitions — kept as a raw string so this file is also readable
# as plain text and can be diffed cleanly in Git.
# ------------------------------------------------------------------------------

_MACROS = r"""$$
% ===========================================================================
% Threat Surfaces — Course Macro Definitions
% fischer³ Education | assets/macros.py
% Mirrors assets/latex-preamble.tex
% ===========================================================================

% --- Number systems ---
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\C}{\mathbb{C}}

% --- Vectors (bold lowercase) ---
\newcommand{\va}{\boldsymbol{a}}
\newcommand{\vb}{\boldsymbol{b}}
\newcommand{\vc}{\boldsymbol{c}}
\newcommand{\vd}{\boldsymbol{d}}
\newcommand{\ve}{\boldsymbol{e}}
\newcommand{\vf}{\boldsymbol{f}}
\newcommand{\vg}{\boldsymbol{g}}
\newcommand{\vh}{\boldsymbol{h}}
\newcommand{\vi}{\boldsymbol{i}}
\newcommand{\vj}{\boldsymbol{j}}
\newcommand{\vk}{\boldsymbol{k}}
\newcommand{\vn}{\boldsymbol{n}}
\newcommand{\vr}{\boldsymbol{r}}
\newcommand{\vu}{\boldsymbol{u}}
\newcommand{\vv}{\boldsymbol{v}}
\newcommand{\vw}{\boldsymbol{w}}
\newcommand{\vx}{\boldsymbol{x}}
\newcommand{\vy}{\boldsymbol{y}}
\newcommand{\vz}{\boldsymbol{z}}
\newcommand{\vzero}{\boldsymbol{0}}

% --- Statistical vectors ---
\newcommand{\vmu}{\boldsymbol{\mu}}
\newcommand{\vbeta}{\boldsymbol{\beta}}
\newcommand{\vtheta}{\boldsymbol{\theta}}
\newcommand{\veps}{\boldsymbol{\varepsilon}}
\newcommand{\valpha}{\boldsymbol{\alpha}}
\newcommand{\vlambda}{\boldsymbol{\lambda}}
\newcommand{\vsigma}{\boldsymbol{\sigma}}

% --- Matrices (bold uppercase) ---
\newcommand{\mA}{\boldsymbol{A}}
\newcommand{\mB}{\boldsymbol{B}}
\newcommand{\mC}{\boldsymbol{C}}
\newcommand{\mH}{\boldsymbol{H}}
\newcommand{\mI}{\boldsymbol{I}}
\newcommand{\mJ}{\boldsymbol{J}}
\newcommand{\mK}{\boldsymbol{K}}
\newcommand{\mL}{\boldsymbol{L}}
\newcommand{\mQ}{\boldsymbol{Q}}
\newcommand{\mR}{\boldsymbol{R}}
\newcommand{\mS}{\boldsymbol{S}}
\newcommand{\mSigma}{\boldsymbol{\Sigma}}
\newcommand{\mX}{\boldsymbol{X}}
\newcommand{\mY}{\boldsymbol{Y}}

% --- Calculus ---
\newcommand{\pd}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\pdd}[2]{\frac{\partial^2 #1}{\partial #2^2}}
\newcommand{\pdm}[3]{\frac{\partial^2 #1}{\partial #2\,\partial #3}}
\newcommand{\od}[2]{\frac{d #1}{d #2}}
\newcommand{\odd}[2]{\frac{d^2 #1}{d #2^2}}
\newcommand{\grad}{\nabla}
\newcommand{\Grad}[1]{\nabla #1}
\newcommand{\GradP}[2]{\nabla_{#1} #2}
\newcommand{\Div}[1]{\nabla \cdot #1}
\newcommand{\Curl}[1]{\nabla \times #1}
\newcommand{\Lap}[1]{\nabla^2 #1}
\newcommand{\Hess}[1]{\boldsymbol{H}_{#1}}
\newcommand{\Jac}[1]{\boldsymbol{J}_{#1}}

% --- Integral elements ---
\newcommand{\dx}{\,dx}
\newcommand{\dy}{\,dy}
\newcommand{\dz}{\,dz}
\newcommand{\dt}{\,dt}
\newcommand{\dA}{\,dA}
\newcommand{\dV}{\,dV}
\newcommand{\ds}{\,ds}

% --- Linear algebra ---
\newcommand{\T}{^{\top}}
\newcommand{\norm}[1]{\left\|#1\right\|}
\newcommand{\abs}[1]{\left|#1\right|}
\newcommand{\inner}[2]{\langle #1,\, #2 \rangle}
\newcommand{\tr}[1]{\operatorname{tr}\!\left(#1\right)}
\newcommand{\rank}[1]{\operatorname{rank}\!\left(#1\right)}
\newcommand{\diag}[1]{\operatorname{diag}\!\left(#1\right)}
\newcommand{\spn}[1]{\operatorname{span}\!\left\{#1\right\}}
\newcommand{\psd}{\succeq 0}

% --- Statistical notation ---
\newcommand{\E}[1]{\mathbb{E}\!\left[#1\right]}
\newcommand{\Var}[1]{\operatorname{Var}\!\left(#1\right)}
\newcommand{\Cov}[2]{\operatorname{Cov}\!\left(#1,\,#2\right)}
\newcommand{\Cor}[2]{\operatorname{Cor}\!\left(#1,\,#2\right)}
\newcommand{\given}{\,\vert\,}
\newcommand{\iid}{\overset{\text{iid}}{\sim}}
\newcommand{\ind}{\overset{\text{ind}}{\sim}}

% --- Distributions ---
\newcommand{\Normal}{\mathcal{N}}
\newcommand{\MVN}[2]{\mathcal{N}\!\left(#1,\,#2\right)}
\newcommand{\Bern}{\operatorname{Bernoulli}}
\newcommand{\Bin}{\operatorname{Binomial}}
\newcommand{\Pois}{\operatorname{Poisson}}
\newcommand{\Unif}{\operatorname{Uniform}}
\newcommand{\Gam}{\operatorname{Gamma}}
\newcommand{\Beta}{\operatorname{Beta}}

% --- Likelihood & inference ---
\newcommand{\Lik}{\mathcal{L}}
\newcommand{\loglik}{\ell}
\newcommand{\Score}[1]{s(#1)}
\newcommand{\FI}{\mathcal{I}}
\newcommand{\MLE}[1]{\hat{#1}_{\text{MLE}}}
\newcommand{\MAP}[1]{\hat{#1}_{\text{MAP}}}
\newcommand{\posterior}{p(\vtheta \given \vx)}
\newcommand{\prior}{p(\vtheta)}
\newcommand{\likelihood}{p(\vx \given \vtheta)}
\newcommand{\KL}[2]{D_{\text{KL}}\!\left(#1\,\|\,#2\right)}

% --- Miscellaneous ---
\newcommand{\defeq}{\coloneqq}
\newcommand{\st}{\text{ s.t. }}
\newcommand{\BigO}[1]{\mathcal{O}\!\left(#1\right)}
\newcommand{\sigmoid}[1]{\sigma\!\left(#1\right)}
$$"""


def inject():
    """
    Inject course MathJax macros into the current notebook output.
    The $$...$$ block is processed by MathJax and renders invisibly —
    it defines the macros without displaying anything to the reader.

    Call this once at the top of every notebook, after the setup cell.
    """
    display(Markdown(_MACROS))
