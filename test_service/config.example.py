"""Configurable parameters for the application

Author: Alexander Hultnér, 2017

This module store configurable python parameters set by the end user.
Rename rename your configuration file to config.py and do not push your changes
upstream.

Generate a good secret using the following code
import os
os.urandom(24)
This can also be invoked from commandline by the following code
python3 -c "import os; print(os.urandom(24))"

Attributes:
    SESSION_SECRET (str): Key used to encrypt sessions
    DB_USER (str): PostgreSQL user
    DB_PASSWORD (str): PostgreSQL password, empty if peer auth
    DB_DATABASE (str): Database to work against
    DB_SCHEMA (str): Not sure if this should be configurable, target schema
    DB_HOST (str): Database server, default is localhost
    DB_PORT (int): Port the database server is running on
"""

SESSION_SECRET = 'CHANGE ME'

"""Database connection configuration """
DB_USER = 'postgres'
DB_PASSWORD = ''
DB_DATABASE = 'experiment'
DB_SCHEMA = 'notes'
DB_HOST = 'localhost'
DB_PORT = 5432
