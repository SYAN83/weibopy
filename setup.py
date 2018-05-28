import setuptools
import re


APP_NAME = "weibopy"

# Get long description
with open("README.md", "r") as fh:
    long_description = fh.read()

# Get the version
version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('weibopy/__init__.py', 'r') as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        VERSION = match.group(1)
    else:
        raise RuntimeError("No version number found!")


setuptools.setup(
    name=APP_NAME,
    version=VERSION,
    author="Shu Yan, Chuan Hong",
    author_email="yanshu.usc@gmail.com",
    description="An easy-to-use Python library for accessing the Sina Weibo API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SYAN83/weibopy",
    packages=setuptools.find_packages(exclude=['tests']),
    python_requires=">=3.4",
    install_requires=[
        "requests>=2.11.1",
        "requests_oauthlib>=0.8.0",
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)