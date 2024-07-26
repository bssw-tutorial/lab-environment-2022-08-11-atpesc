#!/usr/bin/env python

"""
A do nothing test suite.  I just want dots printing out when the package's
test suite runs.
"""

import time
import unittest

from pathlib import Path

import mytool

TESTS_PATH = Path(__file__).parent
TEST_DATA_PATH = TESTS_PATH.joinpath('TestData').resolve()
PKG_DATA_PATH = TESTS_PATH.joinpath('..', 'PkgData').resolve()

class Test1(unittest.TestCase):
    def setUp( self ):
        pass

    def tearDown(self):
        pass

    def testA(self):
        #self.assertTrue(False)
        time.sleep(0.25)

    def testB(self):
        self.assertTrue(True)
        time.sleep(0.5)

    def testC(self):
        time.sleep(0.125)

    def testD(self):
        time.sleep(0.25)
