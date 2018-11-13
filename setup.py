from setuptools import setup, find_packages
from pkg_resources import parse_version
from distutils.command.build import build as _build
import os.path
import re

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

from distutils.command.build import build as _build

class Builder(_build):
    def run(self):
        from babel.messages.frontend import compile_catalog
        print(os.getcwd(), self.distribution.get_option_dict('compile_catalog'))
        compiler = compile_catalog(self.distribution)
        compiler.domain = ["argparse"]
        os.makedirs(os.path.join(self.build_lib, NAME, "locale",
                                 "fr", "LC_MESSAGES"),
                  exist_ok=True)
        compiler.directory = os.path.join(self.build_lib, NAME, "locale")
        compiler.input_file = os.path.join("src", "argparse_fr.po")
        compiler.locale = "fr"
        compiler.run()
        _build.run(self)
        
setup(
    name=NAME,
    version = VERSION,
    description = "Provides translations for argparse module",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = find_packages(exclude = ["tests", "docs", "src"]),
    author="s-ball",
    author_email = "s-ball@laposte.net",
    url = "https://github.com/s-ball/i18nparse",
    license = "MIT License",
    project_urls = {
        "Changelog":
            "https://github.com/s-ball/i18n/blob/master/CHANGES.txt"
        },
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
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
    test_suite = "tests",
    package_data = { "": ["LICEN[CS]E*", "locale/*/*/*.mo"]},
    install_requires = ["babel"],
    setup_requires = ["babel"],
    cmdclass = {"build": Builder},
    )
