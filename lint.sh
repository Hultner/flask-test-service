#!/usr/bin/env sh

## DESCRIPTION: Check Python code for PEP 8 coding style adherence 
## AUTHOR: Alexander Hultnér <alexander@cetrez.com>
## USAGE: ./lint.sh

# Find all .py files which are not from virtualenv and run pycodestyle on them
find . -iname "*.py" \
    -not -path "./flask-test-service/*" \
    -exec echo "{}:" \; \
    -exec flake8 {} \; \
    -exec pylint {} \;
