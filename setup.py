from setuptools import setup, find_packages

from claripy import __version__

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="claripy-sdk",
    description="Python SDK for use with Clarity.io sensors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,

    url="https://github.com/rogers-obrien-rad/clarity-python-sdk",
    author_email="hfritz@r-o.com",

    py_modules=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "python-dotenv",
    ]
)