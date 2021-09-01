#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup
from distutils.extension import Extension

import sys

if sys.version_info < (3,4):
    print('Python 3.4 is required', file=sys.stderr)
    sys.exit(1)

setup(
    name='wrf2simra',
    version='0.0.1',
    description='Convert wrf results to SIMRA',
    maintainer='Arne Morten Kvarving',
    maintainer_email='arne.morten.kvarving@sintef.no',
    packages=['wrf2simra'],
    install_requires=['click', 'numpy', 'siso', 'vtk', 'scipy'],
    entry_points={
        'console_scripts': [
            'wrf2simra=wrf2simra.__main__:main'
        ],
    },
)
