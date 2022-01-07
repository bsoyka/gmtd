# Give Me the Docs

**Give Me the Docs** finds the docs for Python packages so you don't have to.

```console
$ gmtd numpy
Found documentation for numpy:

    - https://numpy.org/doc/1.21
    - https://www.numpy.org
```

[![Downloads](https://pepy.tech/badge/gmtd)](https://pepy.tech/project/gmtd)
[![Supported Versions](https://img.shields.io/pypi/pyversions/gmtd.svg)](https://pypi.org/project/gmtd)
[![License](https://img.shields.io/pypi/l/gmtd)](https://github.com/bsoyka/gmtd/blob/master/LICENSE)
[![Version](https://img.shields.io/pypi/v/gmtd?label=latest)](https://pypi.org/project/gmtd)

## Installation

Give Me the Docs is available on PyPI:

```console
$ pip install gmtd
```

Give Me the Docs officially supports Python 3.8+.

## API Reference

### `gmtd.get_documentation(package_name)`

Gets the documentation URL for a package.

#### Args
* **`package`** *(`str`)*: The name of the package to get documentation for.

#### Returns:
*(`List[str]`)*: A list of possible documentation URLs for the package, ordered from most to
least likely to be official documentation.

#### Raises:
* **`PackageNotFoundError`**: If the package is not installed.
