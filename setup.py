import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="uMath",
    version="1.0.0",
    description="It provides some useful math functions",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/UsmanMaan324/uMath",
    author="Usman Ali",
    author_email="usmanalianjum04@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["UsmanMath"],
    include_package_data=True,
    install_requires=[],
)
