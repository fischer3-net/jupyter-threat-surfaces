# ==============================================================================
# Standard setup cell — Threat Surfaces | fischer³ Education
# Paste this as the first CODE cell in every notebook.
# It handles both local execution and Google Colab automatically.
# ==============================================================================

import sys

# ------------------------------------------------------------------------------
# Detect environment and load macros from the single source of truth
# ------------------------------------------------------------------------------
_MACROS_URL = (
    "https://raw.githubusercontent.com/fischer3-net/jupyter-threat-surfaces"
    "/main/assets/macros.py"
)

if "google.colab" in sys.modules:
    # Colab: fetch macros.py directly from GitHub and execute it
    import urllib.request
    exec(urllib.request.urlopen(_MACROS_URL).read().decode())
else:
    # Local / JupyterLab / VS Code: import from the repo on disk
    import sys, os
    # Ensure repo root is on the path regardless of where the notebook lives
    _repo_root = os.path.abspath(os.path.join(os.path.dirname("__file__"), "..", ".."))
    if _repo_root not in sys.path:
        sys.path.insert(0, _repo_root)
    from assets.macros import inject

inject()

# ------------------------------------------------------------------------------
# Standard imports for all Threat Surfaces notebooks
# ------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy import optimize, stats, linalg

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "figure.figsize": (9, 6),
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "lines.linewidth": 2,
    "figure.dpi": 120,
})

# Course colour palette — mirrors LaTeX preamble
TS_BLUE  = "#1e64b4"
TS_AMBER = "#c87814"
TS_GREEN = "#1e8c50"
TS_GRAY  = "#64646e"
TS_RED   = "#b41e1e"
TS_LIGHT = "#f5f7fa"

print("Setup complete.")
