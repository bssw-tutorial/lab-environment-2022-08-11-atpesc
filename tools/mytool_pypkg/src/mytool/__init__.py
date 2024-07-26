"""
A minimal, fake python package that exists just as an example custom tool.
We want to print its unittest results in an analysis notebook.
"""

from importlib.metadata import version

__version__ = version("mytool")

# data access
from .load_data import load_data

# ----- Python unittest-based test framework
# Used for automatic test discovery
from .load_tests import load_tests

# Allow users to run full test suite as mytool.test()
from .test import test
