#!/usr/bin/env bash


set -euo pipefail


cd "$(dirname "$0")/.."
echo "-- Build Logging package --"
gnome-terminal -- bash -c "sudo ./scripts/helpers/_build.sh $*"