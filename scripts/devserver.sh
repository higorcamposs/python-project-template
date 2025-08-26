#!/usr/bin/env bash
set -euo pipefail

[ -f ".venv/bin/activate" ] && source .venv/bin/activate
[ -f ".env" ] && export $(grep -v '^#' .env | xargs) || true

python -m my_project "$@"
