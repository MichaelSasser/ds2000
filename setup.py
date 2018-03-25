#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2018  Michael Sasser <Michael@MichaelSasser.de>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from codecs import open
from os import path

from setuptools import find_packages, setup

from ds2000._version import __version__

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.de"

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Python Packaging and Distributing: https://packaging.python.org/tutorials/distributing-packages/#setup-py
setup(
    name='ds2000',
    version=__version__,
    description='TODO',
    long_description=long_description,
    url='https://github.com/MichaelSasser/pyhexedit',
    author='Michael Sasser',
    author_email='Michael@MichaelSasser.de',
    license='GPLv3+',
    classifiers=[
        # Look here for all Classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Environment :: Console',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
        'Topic :: Other/Nonlisted Topic',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    keywords='oscilloscope rigol ds2000 terminal package library lib',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires='>=3.6',
)
