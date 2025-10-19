import unittest
from CryptoAlgorithms.algorithms.tests.RNGEncryptorTestsSuite import RNGEncryptorTestSuite
from CryptoAlgorithms.algorithms.tests.RNGTestsSuite import RNGTestSuite


def suite():
    suite = unittest.TestSuite()
    suite.addTest(RNGTestSuite())
    suite.addTest(RNGEncryptorTestSuite())
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())