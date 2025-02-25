#!/usr/bin/python

from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

README = path.abspath(path.join(path.dirname(__file__), 'README.rst'))
desc = 'A Python logging handler for Fluentd event collector'

setup(
  name='fluent-logger',
  version='0.10.0',
  description=desc,
  long_description=open(README).read(),
  package_dir={'fluent': 'fluent'},
  packages=['fluent'],
  install_requires=['msgpack>1.0'],
  author='Kazuki Ohta',
  author_email='kazuki.ohta@gmail.com',
  maintainer='Arcadiy Ivanov',
  maintainer_email='arcadiy@ivanov.biz',
  url='https://github.com/fluent/fluent-logger-python',
  download_url='https://pypi.org/project/fluent-logger/',
  license='Apache License, Version 2.0',
  classifiers=[
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Development Status :: 5 - Production/Stable',
    'Topic :: System :: Logging',
    'Intended Audience :: Developers',
  ],
  python_requires='>=3.5',
  test_suite='tests'
)
