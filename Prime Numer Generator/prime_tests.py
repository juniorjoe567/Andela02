import unittest
from primes import PrimeGenerator

class PrimeGeneratorTests(unittest.TestCase):

    """ Testing whether all returned numbers are prime """
    def test_primes(self):
        self.assertEqual(PrimeGenerator(10).prime_generator(), [2, 3, 5, 7])
        self.assertEqual(PrimeGenerator(20).prime_generator(), [2, 3, 5, 7, 11, 13, 17, 19])

    """ Testing for zero """
    def test_zero(self):
        self.assertEqual(PrimeGenerator(0).prime_generator(), "Zero is not prime")
