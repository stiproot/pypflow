from setuptools import setup, find_packages

# metadata...
name = "pypflow"
description = "A simple workflow management framework for Python."
author = "Simon Stipcich"
author_email = "stipcich.simon@gmail.com"
url = "https://github.com/stiproot/pypflow"
license = "MIT"
keywords = ["python", "package", "workflow", "beta"]
version = "0.0.1"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# dependencies...
install_requires = []

# setup...
setup(
    name=name,
    version=version,
    packages=find_packages(where="src"),
    package_dir={"pypflow": "src/pypflow"},
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    keywords=keywords,
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
)
