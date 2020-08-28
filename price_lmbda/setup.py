#!/usr/bin/python3

from setuptools import setup, find_packages
import pathlib

tests_requires = []

setup(
        name='price_function',
        version='0.0.1',
        packages=find_packages(where='src'),
        install_requires=[],
        test_require=tests_requires
        )
