#!/usr/bin/env bash
set -euo pipefail

git add .
git commit -m "$(date)"
git pull --rebase
git push
