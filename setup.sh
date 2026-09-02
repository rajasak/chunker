#!/bin/bash

set -e

echo ""
echo "======================================"
echo "   CHUNKER AUTO INSTALL STARTED"
echo "======================================"

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"

echo "Repository: $REPO_ROOT"
echo ""

echo "Creating Python virtual environment..."

python -m venv "$REPO_ROOT/.venv"

echo "Installing pandas and numpy..."

"$REPO_ROOT/.venv/Scripts/python.exe" -m pip install --upgrade pip
"$REPO_ROOT/.venv/Scripts/python.exe" -m pip install pandas numpy

echo ""
echo "======================================"
echo "   INSTALLATION COMPLETE"
echo "======================================"

echo ""
echo "Virtual environment created at:"
echo "$REPO_ROOT/.venv"
