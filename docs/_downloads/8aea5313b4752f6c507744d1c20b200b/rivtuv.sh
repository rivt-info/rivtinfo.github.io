#!/usr/bin/env bash
set -euo pipefail
# Echo commands for visibility
set -x

# macOS / POSIX translation of rivtuv.cmd
# 1) clear any existing project and venv
# 2) create new venv
# 3) install rivt from GitHub
# 4) download example files from GitHub

rvfolder="rivt-doc2"

# go to home directory
cd "$HOME"

# try to deactivate any existing uv venv (if uv is installed)
if command -v uv >/dev/null 2>&1; then
  uv deactivate || true
fi

# remove old project folder
rm -rf "$rvfolder"

# clean uv cache if available
if command -v uv >/dev/null 2>&1; then
  uv cache clean || true
fi

# set up project folder
mkdir -p "$rvfolder"
cd "$rvfolder"

# create venv (prefer uv helper if present)
if command -v uv >/dev/null 2>&1; then
  uv venv
else
  python3 -m venv .venv
fi

# activate venv
if [ -f ".venv/bin/activate" ]; then
  # shellcheck disable=SC1090
  source .venv/bin/activate
fi

# install rivt from GitHub (use uv pip if available)
if command -v uv >/dev/null 2>&1; then
  uv pip install --upgrade git+https://github.com/rivtlib-dev/rivtlib.git@main
else
  pip install --upgrade git+https://github.com/rivtlib-dev/rivtlib.git@main
fi

# download example project into new folder
mkdir -p example2
cd example2

# Use -L to follow redirects and download raw files
curl -L https://raw.githubusercontent.com/rivt-info/rivt-single-doc/main/rv000-single-doc.py -O
curl -L https://raw.githubusercontent.com/rivt-info/rivt-single-doc/main/s-beam1-v.csv -O
curl -L https://raw.githubusercontent.com/rivt-info/rivt-single-doc/main/s-sectprop.py -O
curl -L https://raw.githubusercontent.com/rivt-info/rivt-single-doc/main/s-beam.png -O

echo
echo "Setup complete. To run the example (inside the activated venv):"
echo "  python rv000-single-doc.py"
echo
echo "If you want an interactive shell after this script finishes, run:"
echo "  exec \$SHELL"
echo
