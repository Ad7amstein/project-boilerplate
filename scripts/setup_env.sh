#!/bin/bash

# Bootstrap uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "📥 Installing 'uv'..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Add uv to PATH for the rest of this script
    export PATH="$HOME/.local/bin:$PATH"
fi

# Default Python version
DEFAULT_PYTHON_VERSION="3.12"

# Allow user to specify Python version (optional)
PYTHON_VERSION=${1:-$DEFAULT_PYTHON_VERSION}

# Check if the virtual environment exists
if [ -d ".venv" ]; then
    echo "✅ Virtual environment already exists. Activating..."
else
    echo "🆕 Creating virtual environment using Python ${PYTHON_VERSION}..."
    uv venv .venv --python "${PYTHON_VERSION}"
fi

# Activate the environment
echo "🚀 Activating virtual environment..."
# shellcheck disable=SC1091
source .venv/bin/activate

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies from requirements.txt..."
    uv pip install -r requirements.txt
else
    echo "⚠️  No requirements.txt found. Skipping dependency installation."
fi

# Install the current package in editable mode
echo "🔧 Installing the current package in editable mode..."
if [ ! -f "setup.py" ] && [ ! -f "pyproject.toml" ]; then
    echo "❌ No setup.py or pyproject.toml found. Cannot install package in editable mode."
    exit 1
fi
uv pip install -e .

echo "✅ Environment setup complete!"
