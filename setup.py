#!/usr/bin/env python

from codecs import open

from setuptools import setup, find_packages

def read(f):
    return open(f, encoding='utf-8').read()

setup(name='typeguess',
      version='0.0.1',
      description='Data type guesser',
      long_description=read('README.rst'),
      author='Rylan Santinon',
      author_email='rylans@gmail.com',
      url='https://github.com/rylans/typeguess',
      keywords=['typeguess', 'type guesser', 'datatype guesser'],
      license='Apache 2.0',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Utilities'],
      packages=find_packages())
