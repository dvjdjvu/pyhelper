#!/usr/bin/env python3
#encoding: UTF-8

from setuptools import setup, find_packages

PACKAGE = "help"
NAME = "help"
DESCRIPTION = "Library help for python"
AUTHOR = "dvjdvju"
AUTHOR_EMAIL = "djvu@inbox.ru"
URL = "git@github.com:dvjdjvu/pyhelp.git"
VERSION = __import__(PACKAGE).__version__
 
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)