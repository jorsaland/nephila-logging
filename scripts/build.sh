#!/usr/bin/env bash


set -euo pipefail


echo "=== Nephila Logging ===\n"


source ./env/bin/activate
pip install . --force-reinstall