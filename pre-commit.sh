#!/usr/bin/env bash

set -e

black ./
isort ./
flake8

python runtests.py
