#!/usr/bin/env bash
set -euo pipefail

git add .
msg="$(date)"
[ -n "${1:-}" ] && msg="$msg: $1"
git commit -m "$msg"
git pull --rebase
git push
