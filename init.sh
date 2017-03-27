#!/usr/bin/env sh

# Initiate the virtual environment for application and install dependencies

# Install virtualenv
pip3 install virtualenv

# Initiate project
virtualenv -p python3 flask-test-service

# Activate environment and install requirements
source activate.sh
pip install -r requirements.txt

