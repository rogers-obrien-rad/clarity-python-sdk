![last_commit](https://img.shields.io/github/last-commit/rogers-obrien-rad/clarity-python-sdk)
[![test suite](https://github.com/rogers-obrien-rad/package-template/actions/workflows/tests.yml/badge.svg)](https://github.com/rogers-obrien-rad/package-template/actions/workflows/tests.yml)

# Clarity.io Python SDK
SDK to access Clarity.io API resources

## Installation
_The SDK is currently under development_

## Usage
Please see the [Snippets](https://github.com/rogers-obrien-rad/clarity-python-sdk/tree/main/snippets) directory to see sample use cases. Below is the general use case:

```python
import os
from claripy.clarity import Clarity

connection = Clarity(os.getenv("API_KEY"))

latest_data_by_min = connection.__measurements__.get()
devices = connection.__devices__.get()
sources = connection.__datasources__.get()
```

To create a `Clarity` object, simply pass the API key as a parameter. You then have access to data from the three Clarity endpoints: measurements, devices, and datasources. 

## Resources
* [Clarity.io](https://www.clarity.io/)
* [Clarity.io Dashboard](https://dashboard.clarity.io/overview)
* [Clarity.io API Documentation](https://api-guide.clarity.io/)

## License
This repository is licensed under the [Apache License](https://github.com/rogers-obrien-rad/clarity-python-sdk/blob/main/LICENSE)

## Contributing
![contributing](https://img.shields.io/github/contributors/rogers-obrien-rad/clarity-python-sdk)
