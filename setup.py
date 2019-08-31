#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt', 'r') as r:
    requires = r.read().split()

with open('README.rst', 'r') as r:
    readme = r.read()

setup(
    name='alignment',
    version='0.1',
    author="Linus Kohl",
    packages=["alignment"],
    author_email="linus@munichresearch.com",
    python_requires='>=3.6',
    license='GPLv3',
    long_description=readme,
    install_requires=requires,
)
