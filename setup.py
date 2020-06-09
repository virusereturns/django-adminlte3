#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

setup(
    name='django-adminlte3',
    version='0.1.6',
    author='d3n1z',
    author_email='d3n1z@protonmail.com',
    packages=['adminlte3', 'adminlte3_theme'],
    url='https://github.com/virusereturns/django-adminlte3',
    license='MIT',
    description='Admin LTE templates, admin theme, and template tags for Django',
    include_package_data=True,
)
