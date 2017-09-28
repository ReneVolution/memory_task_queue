#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from codecs import open
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='memory_task_queue',
    version='0.0.1',
    packages=['memory_task_queue', 'memory_task_queue.tests'],
    url='',
    license='MIT',
    author='René Calles',
    author_email='info@renevolution.com',
    description='A Task Queue running on memory.',
    long_description=long_description,
    setup_requires=['pytest-runner'],
    test_suite='pytest',
    tests_require=['pytest', 'mock'],
)
