#!/usr/bin/env bash
# Script: run_data.sh
# Purpose: generate data/problems.json used by index.html
# Usage: ./run_data.sh

set -e
# Ensure we are in the repo root
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$SCRIPT_DIR"
python3 generate_data.py
