from setuptools import setup, find_packages

from claripy.clarity import __version__

setup(
    name="claripy-sdk",
    description="Python SDK for use with Clarity.io sensors",
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