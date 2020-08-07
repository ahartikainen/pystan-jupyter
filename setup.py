import codecs
import os
import re

import setuptools
from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
REQUIREMENTS_FILE = os.path.join(PROJECT_ROOT, "requirements.txt")
README_FILE = os.path.join(PROJECT_ROOT, "README.md")


def get_requirements():
    with codecs.open(REQUIREMENTS_FILE) as buff:
        return buff.read().splitlines()


def get_long_description():
    with codecs.open(README_FILE, "rt") as buff:
        return buff.read()


setup(
    name="pystan-jupyter",
    license="ISC",
    version="0.1b1",
    description="Enable PyStan3 use on Jupyter Notebook/Lab.",
    author="Ari Hartikainen",
    url="https://github.com/ahartikainen/pystan-jupyter",
    packages=find_packages(),
    install_requires=get_requirements(),
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
)
