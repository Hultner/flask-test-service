"""This is a testing application

Author: Alexander Hultnér, 2017

This application is mainly used for testing the current state of flask and it's
capabilities.
"""
from flask import (Flask,
                   url_for)
from test_service import config

app = Flask(__name__)  # pylint: disable=invalid-name
app.secret_key = config.SESSION_SECRET
from test_service import routes  # pylint: disable=wrong-import-position

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
