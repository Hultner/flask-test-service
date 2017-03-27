#!/usr/bin/env sh

# Activate virtual envriontment
source ./flask-test-service/bin/activate

# Flask entry point
export FLASK_APP=app.py

# Run application allowing external requests
python3 -m flask run --host=0.0.0.0
