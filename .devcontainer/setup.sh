#!/usr/bin/env bash
set -euo pipefail

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Create & activate venv
uv venv .venv
. .venv/bin/activate

# Install CPU-only torch first
uv pip install --index-url https://download.pytorch.org/whl/cpu "torch>=2.2,<3"

# Install the rest of your deps from PyPI
uv pip install -r requirements.txt

# Install Jupyter + kernel
uv pip install jupyterlab ipykernel
python -m ipykernel install --user --name COMPSS-211A --display-name "Python (COMPSS-211A)"