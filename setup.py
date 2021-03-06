# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import io

import pymerkle

from setuptools import find_packages
from setuptools import setup

SOURCE_DIR   = "pymerkle"
DESCRIPTION  = pymerkle.__doc__.rstrip()
EXCLUDE      = ("benchmarks", "docs", "tests",)
AUTHOR       = "FoteinosMerg"
AUTHOR_EMAIL = "foteinosmerg@protonmail.com"
URL          = "https://github.com/FoteinosMerg/pymerkle"
PROJECT_URLS = {
    "github": URL,
    "source": "%s/%s" % (URL, "tree/master/%s" % pymerkle.__name__),
    "docs": "https://%s.readthedocs.io/en/latest/" % pymerkle.__name__
}
README       = "README.md"
CONTENT_TYPE = "text/markdown"
REQUIREMENTS = "requirements.txt"
PYTHON       = ">=3.6"
LICENSE      = "License :: OSI Approved :: MIT License"
KEYWORDS     =  [
    "audit", "consistency", "merkle", "proof"
]
CLASSIFIERS  =  [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3.6",
    # "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Security :: Cryptography",
    "Topic :: Software Development :: Libraries :: Python Modules"
]

LONG_DESCRIPTION = ""
INSTALL_REQUIRES = []

current_dir = os.path.abspath(os.path.dirname(__file__))

try:
  with open(os.path.join(current_dir, README), "r") as _file:
    LONG_DESCRIPTION = _file.read()
except FileNotFoundError:
    pass

try:
  with io.open(os.path.join(current_dir, REQUIREMENTS), encoding="utf-8") as _file:
    INSTALL_REQUIRES = [_.strip() for _ in _file.readlines()]
except FileNotFoundError:
    INSTALL_REQUIRES = [
          "tqdm>=4.28.1"
      ]

setup(
    name=pymerkle.__name__,
    version=pymerkle.__version__,
    description=DESCRIPTION,
    url=URL,
    project_urls=PROJECT_URLS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=CONTENT_TYPE,
    packages=find_packages(SOURCE_DIR, exclude=EXCLUDE),
    python_requires=PYTHON,
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    license=LICENSE
)
