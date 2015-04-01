#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="ruralpowerproject",
    version="0.1.1",
    author="Antoine Claval",
    author_email="tech@ruralpowerproject.org",
    packages=[
        "ruralpowerproject",
    ],
    include_package_data=True,
    install_requires=[
        "Django==1.7.6",
    ],
    zip_safe=False,
    scripts=["ruralpowerproject/manage.py"],
)
