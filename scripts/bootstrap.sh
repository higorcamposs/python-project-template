#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .[dev]

# pre-commit opcional
if command -v pre-commit >/dev/null 2>&1; then
  pre-commit install || true
fi

echo "Ambiente pronto! Ative com: source .venv/bin/activate"
