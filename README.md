<h1 align="center"> LinkStatus </h1>
<h2 align="center"> Check link status</h2>

<p align="center">
    <a href="https://pypi.org/project/linkstatus"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/linkstatus.svg?style=flat"></a>
    <a href="https://travis-ci.com/pythonpune/linkstatus"><img alt="Build Status"
    src="https://travis-ci.com/pythonpune/linkstatus.svg?branch=master"></a>
    <a href="https://github.com/pythonpune/linkstatus/blob/master/LICENSE"><img alt="License: GPLv3" src="https://img.shields.io/pypi/l/linkstatus.svg?version=latest"></a>
    <a href="https://pypi.org/project/linkstatus/#history"><img alt="PyPI version" src="https://badge.fury.io/py/linkstatus.svg"></a>
    <a href="https://pepy.tech/project/linkstatus"><img alt="Downloads" src="https://pepy.tech/badge/linkstatus"></a>
    <a href="https://pypi.org/project/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

This is simple link status checker for text/markdown files.

### Install

- pip

    ```bash
    pip install linkstatus --user
    ```

- source

    ```bash
    pip install . --user
    ```

### Usage:
```bash
❯❯❯ linkstatus --help
Usage: linkstatus [OPTIONS] [SOURCE]...

  Check Link Status

Options:
  -r, --recursive        Include all files from directories recursively
  -t, --timeout INTEGER  Request timeout (default 4 second)
  -rt, --retry INTEGER   Retry link status (default 2 time)
  --help                 Show this message and exit.
```

![linkstatus](https://user-images.githubusercontent.com/11618054/67764478-0fcec100-fa70-11e9-9c3c-04c1f432f620.png)


**Note: Skip link check for any line by adding `noqa` (no quality assurance) as inline comment
.** like `<-- noqa -->` for `html` and `markdown`, `#noqa` for `python` etc...

### CONTRIBUTION GUIDELINES

If you would like to contribute please read the project contribution guidelines [here](CONTRIBUTING.md).

### CODE OF CONDUCT

For the community code of conduct please follow the following [link](https://github.com/pythonpune/meetup-talks/blob/master/CODE_OF_CONDUCT.md).
