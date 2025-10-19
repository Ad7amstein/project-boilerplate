#!/bin/bash

# Default Python version
DEFAULT_PYTHON_VERSION="3.12"

# Allow user to specify Python version (optional)
PYTHON_VERSION=${1:-$DEFAULT_PYTHON_VERSION}

# Locate Python binary
PYTHON_BIN=$(command -v python${PYTHON_VERSION})

# Check if the chosen Python version exists
if [ -z "$PYTHON_BIN" ]; then
    echo "❌ Python ${PYTHON_VERSION} not found. Please install it first."
    exit 1
fi

# Check if the virtual environment exists
if [ -d ".venv" ]; then
    echo "✅ Virtual environment already exists. Activating..."
else
    echo "🆕 Creating virtual environment using Python ${PYTHON_VERSION}..."
    "$PYTHON_BIN" -m venv .venv
fi

# Activate the environment
echo "🚀 Activating virtual environment..."
source .venv/bin/activate
