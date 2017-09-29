"""This is a testing application

This application is mainly used for testing the current state of flask and it's
capabilities.
"""
from setuptools import setup

setup(
    name='test_service',
    version='0.0.1',
    packages=['test_service'],
    author='Alexander Hultnér',
    description=('Testing ground for using flask for driving a service in '
                 'a microservice architecture'),
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
        'sqlalchemy',
        'psycopg',
    ],
)
