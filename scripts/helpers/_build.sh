#!/usr/bin/env bash


set -euo pipefail


breakpoint() {
    if [[ " ${*} " == *" debug "* ]]; then
        read -rp $'\n=== ENTER to exit ==='
    fi
}
trap 'breakpoint "$@"' EXIT


echo "=== Nephila Logging ===\n"

source ./env/bin/activate
pip install . --force-reinstall
python setup.py sdist