
#!/bin/bash

set -e

echo ""
echo "======================================"
echo "   CHUNKER AUTO INSTALL STARTED"
echo "======================================"

echo "Creating Python virtual environment..."

python3 -m venv .venv

echo "Activating virtual environment..."

source .venv/bin/activate

echo "Installing pandas and numpy..."

python -m pip install --upgrade pip
python -m pip install pandas numpy

echo ""
echo "======================================"
echo "   INSTALLATION COMPLETE"
echo "======================================"
echo ""
echo "Virtual environment: .venv"
echo "Activate it with:"
echo "source .venv/bin/activate"
echo ""
