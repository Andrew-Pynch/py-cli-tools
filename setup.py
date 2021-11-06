import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="py-cli-tools",
    version="1.0.1",
    description="Functions that I found myself writing in different projects over and over again go here",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Andrew-Pynch/py-cli-tools",
    author="Andrew Pynch",
    author_email="andrewpynchbusiness@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pyclitools=pyclitools.__main__",
        ]
    },
)
