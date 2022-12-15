#!/usr/bin/env bash
# Runs the PFA development server.
####################
# By Matteo Caravati
####################

set -o errexit # Exit if command failed
set -o pipefail # Exit if pipe failed
set -o nounset # Exit if variable not set
# Remove the initial space and instead use '\n'
IFS=$'\n\t'

# Check if 'venv' directory exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install -U pip

# Pip talks mad shit if I don't install those first
pip install -U ninja
pip install -U setuptools

# Install dependencies
pip install -U -r requirements.txt

# Run the server
python ./server.py