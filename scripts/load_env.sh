#!/usr/bin/env bash
# Helper to load variables from .env into the environment for the current shell.
# Usage: source scripts/load_env.sh

if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
  echo ".env loaded"
else
  echo ".env not found — copy .env.example to .env and add your token"
fi
