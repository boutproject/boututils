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
    # This gives the version if the boututils package was installed
    __version__ = version(__name__)
except PackageNotFoundError:
    # This branch handles the case when boututils is used from the git repo
    try:
        from setuptools_scm import get_version
        from pathlib import Path
        path = Path(__file__).resolve()
        __version__ = get_version(root="..", relative_to=path)
    except (ModuleNotFoundError, LookupError) as e:
        # ModuleNotFoundError if setuptools_scm is not installed.
        # LookupError if git is not installed, or the code is not in a git repo even
        # though it has not been installed.
        from warnings import warn
        warn(
            "'setuptools_scm' and git are required to get the version number when "
            "running boututils from the git repo. Please install 'setuptools_scm' and "
            "check 'git rev-parse HEAD' works. Setting __version__='dev' as a "
            "workaround."
        )
        __version__ = "dev"
