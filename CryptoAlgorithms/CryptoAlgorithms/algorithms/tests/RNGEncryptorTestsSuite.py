import unittest
from CryptoAlgorithms.algorithms.RNG import RNG
from CryptoAlgorithms.algorithms.RNGEncryptor import RNGEncryptor


#Тесты для генератора случайных чисел
class RNGEncryptorTestSuite(unittest.TestSuite):
    def __init__(self):
        super(RNGEncryptorTestSuite, self).__init__([
            DoubleEncryptedTextShouldBeSame()
        ])

class DoubleEncryptedTextShouldBeSame(unittest.TestCase):
    def runTest(self):
        test_text = "test"

        generator = RNG()

        encryptor = RNGEncryptor(generator)
        encrypted_text = encryptor.encrypt_text(test_text)
        double_encrypted_text = encryptor.encrypt_text(encrypted_text)

        self.assertEqual(test_text, double_encrypted_text.decode("utf-8"))