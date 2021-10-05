#!/usr/bin/env python
import sys
from setuptools import setup
from warnings import warn

if sys.version_info < (3, 7, 0):
    # does 2.7 understand f strings?
    # warn(f"Python version 3.7 or later is required for crdch_model.  Current version: {sys.version_info}")
    warn("Python version 3.7 or later is required for crdch_model.  Current version: " + str(sys.version_info))
    sys.exit(1)

setup(
    version = '1.1.2'
)
