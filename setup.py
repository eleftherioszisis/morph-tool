#!/usr/bin/env python

import imp
import sys

from setuptools import setup, find_packages

if sys.version_info < (2, 7):
    sys.exit("Sorry, Python < 2.7 is not supported")

VERSION = imp.load_source("", "morph_tool/version.py").__version__

setup(
    name="morph-tool",
    author="BlueBrain NSE",
    author_email="bbp-ou-nse@groupes.epfl.ch",
    version=VERSION,
    description="",
    url="https://bbpteam.epfl.ch/project/issues/projects/NSETM/issues",
    download_url="ssh://bbpcode.epfl.ch/nse/morph-tool",
    entry_points={
        'console_scripts': ['morph-tool=morph_tool.cli:cli']},
    license="BBP-internal-confidential",
    install_requires=[
        'click>=6.7',
        'functools32>=3.2;python_version<"3.0"',
        'morphio>=2.1.5',
        'numpy>=1.14',
    ],
    extras_require={
        'all': [
            'bluepyopt>=1.6',
        ]
    },
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
