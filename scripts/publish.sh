#!/usr/bin/env bash
# Build and publish script for local use. Do NOT store your token in this file.
# Usage:
#   source .env            # (or export TWINE_PASSWORD in your shell)
#   ./scripts/publish.sh testpypi   # or 'pypi'

set -euo pipefail

REPO=${1:-testpypi}

echo "Cleaning previous builds..."
rm -rf build dist *.egg-info

echo "Building source and wheel..."
python -m build

echo "Uploading to ${REPO} using twine..."
python -m twine upload --repository ${REPO} dist/*

echo "Done."
