#!/usr/bin/env bash
set -euo pipefail

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Create & activate venv
uv venv .venv
. .venv/bin/activate

# Deps (CPU torch is fine on PyPI)
uv pip install -r requirements.txt
uv pip install jupyterlab ipykernel

# Register kernel
python -m ipykernel install --user --name COMPSS-211A --display-name "Python (COMPSS-211A)"