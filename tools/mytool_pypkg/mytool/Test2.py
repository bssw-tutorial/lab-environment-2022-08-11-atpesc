#!/usr/bin/env python

"""
A do nothing test suite.  I just want dots printing out when the package's
test suite runs.
"""

import time
import unittest

from pathlib import Path

import mytool

FILE_PATH = Path(__file__).parent
TEST_PATH = FILE_PATH.joinpath('TestData')
DATA_PATH = FILE_PATH.joinpath('PkgData')

class Test1(unittest.TestCase):
    def setUp( self ):
        pass

    def tearDown(self):
        pass

    def testA(self):
        time.sleep(0.125)

    def testB(self):
        time.sleep(0.25)

    def testC(self):
        time.sleep(0.35)

def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( Test1 ) )
    
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner( verbosity=2 ).run( suite() )

