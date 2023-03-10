#!/usr/bin/env bash
# Description: Clean up the project

# Usage: ./clean.sh [options]
# Options:
#   -h,  --help   Show this help message and exit
#   -py, --python Remove all Python virtual environments
#   -no, --node   Remove all node_modules directories
#   -js, --js     Remove all files and directories in web/static/js except .keep

set -o errexit # Exit if command failed
set -o pipefail # Exit if pipe failed
# Remove the initial space and instead use '\n'
IFS=$'\n\t'

# Parse arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -h|--help)
            grep '^# Usage:' "$0" | cut -c 3-
            exit 0
            ;;
        -py|--python)
            PY=true
            shift
            ;;
        -no|--node)
            NO=true
            shift
            ;;
        -js|--js)
            JS=true
            shift
            ;;
        *)
            echo "Unknown option: $key"
            exit 1
            ;;
    esac
done

if [[ -v PY ]]; then
    # Remove all Python virtual environments
    echo "[*] Removing all Python virtual environments..."
    find . -name "venv" -type d -exec rm -rf {} +
fi

if [[ -v NO ]]; then
    # Remove all node_modules directories
    echo "[*] Removing all node_modules directories..."
    find . -name "node_modules" -type d -exec rm -rf {} +
fi

if [[ -v JS ]]; then
    # Remove all files and directories in web/static/js except .keep
    echo "[*] Removing all files and directories in web/static/js except .keep..."
    find web/static/js -mindepth 1 -maxdepth 1 -not -name ".keep" -exec rm -rf {} +
fi