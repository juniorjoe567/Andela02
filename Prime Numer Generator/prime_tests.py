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

    """ Testing for one """
    def test_one(self):
        self.assertEqual(PrimeGenerator(1).prime_generator(), "One is not prime")

    """ Testing for a non-integer """
    def test_non_integer(self):
        self.assertEqual(PrimeGenerator("test").prime_generator(), "Input should be an integer")
        self.assertEqual(PrimeGenerator([1,2,3]).prime_generator(), "Input should be an integer")

    """ Testing for negative integers """
    def test_negative(self):
        self.assertEqual(PrimeGenerator(-1).prime_generator(), "Input should be a positive integer")
        self.assertEqual(PrimeGenerator(-50).prime_generator(), "Input should be a positive integer")

if __name__ == '__main__':
    unittest.main()
