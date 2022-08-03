"""
A minimal, fake python package that exists just as an example custom tool.
We want to print its unittest results in an analysis notebook.
"""

import unittest
import nose.core
import pkg_resources

__version__ = pkg_resources.get_distribution('mytool').version

# data access
from mytool.load_data import load_data

# unittests
from mytool.Test1 import suite as suite1
from mytool.Test2 import suite as suite2

def test_suite():
    return unittest.TestSuite([suite1(), suite2()])

def test(verbosity=1):
    if verbosity not in [0, 1, 2]:
        msg = 'Invalid verbosity level - {} not in {0,1,2}'
        raise ValueError(msg.format(verbosity))

    nose.core.TextTestRunner(verbosity=verbosity).run(test_suite())

