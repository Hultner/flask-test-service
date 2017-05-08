#!/usr/bin/env sh

# Activate virtual envriontment
source ./flask-test-service/bin/activate

# Flask entry point
export FLASK_APP=test_service
# Flask debug mode, live code reload and debugger activated
export FLASK_DEBUG=1

# Run application allowing external requests
python3 -m flask run 

