""" Generic routines, useful for all data """

import sys

try:
    from builtins import str
except ImportError:
    raise ImportError("Please install the future module to use Python 2")

# Modules to be imported independent of version
for_all_versions = [\
                    'calculus',\
                    'closest_line',\
                    'datafile',\
                    # 'efit_analyzer',\ # bunch pkg required
                    'fft_deriv',\
                    'fft_integrate',\
                    'file_import',\
                    'int_func',\
                    'linear_regression',\
                    'mode_structure',\
                    # 'moment_xyzt',\   # bunch pkg requried
                    'run_wrapper',\
                    'shell',\
                    'showdata',\
                    # 'surface_average',\
                    # 'volume_integral',\ #bunch pkg required
                    ]

# Check the current python version
if sys.version_info[0]>=3:
    do_import = for_all_versions
    __all__ = do_import
else:
    do_import = for_all_versions
    do_import.append('anim')
    do_import.append('plotpolslice')
    do_import.append('View3D')
    __all__ = do_import

__name__ = 'boututils'

try:
    from importlib.metadata import version, PackageNotFoundError
except ModuleNotFoundError:
    from importlib_metadata import version, PackageNotFoundError
try:
    __version__ = version(__name__)
except PackageNotFoundError:
    try:
        from setuptools_scm import get_version
    except ModuleNotFoundError as e:
        error_info = (
            "'setuptools_scm' is required to get the version number when running "
            "boututils from the git repo. Please install 'setuptools_scm'."
        )
        print(error_info)
        raise ModuleNotFoundError(str(e) + ". " + error_info)
    else:
        __version__ = get_version(root="..", relative_to=__file__)
