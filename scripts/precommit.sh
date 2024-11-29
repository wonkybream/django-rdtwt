#!/usr/bin/env bash

# Test creation and verification of two certificate chains using oqsprovider for alg $1
set -e
cd $(dirname $0) && cd ..

source .venv/bin/activate

pip install -r requirements.txt

ruff check --fix --show-fixes
ruff format
