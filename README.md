# boututils

[![Build Status](https://travis-ci.org/boutproject/boututils.svg?branch=master)](https://travis-ci.org/boutproject/boututils)
[![codecov](https://codecov.io/gh/boutproject/boututils/branch/master/graph/badge.svg)](https://codecov.io/gh/boutproject/boututils)
[![Python](https://img.shields.io/badge/python->=3.6-blue.svg)](https://www.python.org/)
[![pypi package](https://badge.fury.io/py/boututils.svg)](https://pypi.org/project/boututils/)
[![PEP8](https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)
[![License](https://img.shields.io/badge/license-LGPL--3.0-blue.svg)](https://github.com/boutproject/boututils/blob/master/LICENSE)

> [!IMPORTANT]
> This has now been merged into [`boutdata`](https://github.com/boutproject/boutdata). Please use that package directly instead.


pip-package of what was previously found in `BOUT-dev/tools/pylib/boututils` Note that
`BOUT-dev/tools/pylib/boututils` was replaced by this repo in
`BOUT++ v4.3.0`.

# Dependencies

`boututils` depends on [`netcfd4`](https://github.com/Unidata/netcdf4-python) which
requires [`HDF5`](https://www.h5py.org) and
[`netcdf-4`](https://github.com/Unidata/netcdf-c/releases) are installed, and that the
`nc-config` utility is in your `PATH`. This can be install with

```
sudo apt-get install libhdf5-serial-dev netcdf-bin libnetcdf-dev
```

in ubuntu

# Install

`pip install boututils`
