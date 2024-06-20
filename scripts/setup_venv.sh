#!/bin/bash
uv venv
source .venv/bin/activate
uv pip install --require-hashes -r requirements_dev.txt