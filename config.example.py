"""Configurable parameters for the application

This module store configurable python parameters set by the end user.
Rename rename your configuration file to config.py and do not push your changes
upstream.

Attributes:
    SESSION_SECRET (str): Key used to encrypt sessions
"""


SESSION_SECRET = 'CHANGE ME'
""" Generate a good secret using the following code
import os
os.urandom(24)
can also be invoked from commandline by the following code
python3 -c "import os; print(os.urandom(24))"
"""
