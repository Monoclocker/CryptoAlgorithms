import unittest
from RNGTestsSuite import RNGTestSuite


def suite():
    suite = unittest.TestSuite()
    suite.addTest(RNGTestSuite())
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())