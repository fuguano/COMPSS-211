#!/usr/bin/env bash
set -euo pipefail

# Quieter uv copies on Codespaces mounts
export UV_LINK_MODE=copy

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Create & activate venv
uv venv .venv
. .venv/bin/activate

# Install pip
uv pip install -U pip

# CPU-only torch (from CPU index only)
uv pip install --index-url https://download.pytorch.org/whl/cpu "torch>=2.2,<3"

# Rest of deps from PyPI
uv pip install -r requirements.txt

# Jupyter + kernel
uv pip install jupyterlab ipykernel
python -m ipykernel install --user --name COMPSS-211A --display-name "Python (COMPSS-211A)"