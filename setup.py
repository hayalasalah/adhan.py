#!/usr/bin/env python
"""
adhan.py - Python library for computing adhan times.

Copyright (C) 2015  Zuhair Parvez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from setuptools import setup

requires = []

setup(
    name='adhan',
    version='0.1.0',
    description='Python library for computing adhan times',
    author='Zuhair Parvez',
    author_email='zuhairparvez@gmail.com',
    url='https://github.com/hayalasalah/adhan.py',
    download_url='https://github.com/hayalasalah/adhan.py/releases/tag/0.1',
    packages=['adhan'],
    install_requires=requires,
    include_package_data=True,
    license='LGPL 3.0',
    keywords=['adhan', 'islam', 'muslim', 'religious'],
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Religion',
    ]
)
