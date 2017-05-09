"""This is a testing application

This application is mainly used for testing the current state of flask and it's
capabilities.
"""
from setuptools import setup

setup(
    name='test_service',
    packages=['test_service'],
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
        'sqlalchemy',
        'psycopg',
    ],
)
