from setuptools import setup, find_packages
from pkg_resources import parse_version
import os.path
import re
import sys

from io import open

NAME = "i18nparse"
with open(os.path.join(os.path.dirname(__file__), NAME,
                       "version.py")) as fd:
    ver_line = next(fd)
    m = re.match(r'\s*__version__\s*=\s*["\"]([^"\"]+)["\"]', ver_line)
    VERSION = m.group(1)

# Base version (removes any pre, post, a, b or rc element)
BASE = parse_version(VERSION).base_version

# In long description, replace "master" in the build status badges
#  with the current version we are building
with open("README.md") as fd:
    long_description = next(fd).replace("master", BASE)
    long_description += next(fd).replace("latest", BASE)
    long_description += "".join(fd)

setup(
    name=NAME,
    version = VERSION,
    description = "Provides translations for argparse module",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = find_packages(exclude = ["src"]),
    author="s-ball",
    author_email = "s-ball@laposte.net",
    url = "https://github.com/s-ball/i18nparse",
    license = "MIT License",
    project_urls = {
        "Changelog":
            "https://github.com/s-ball/i18nparse/blob/master/CHANGES.txt"
        },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Natural Language :: French",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Internationalization",
        ],
    python_requires=">=3",
    package_data = { "": ["locale/*/*/*.mo"]},
    setup_requires = ["mo_installer"],
    locale_src = "src",
    )
