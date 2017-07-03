""" Class that generates prime numbers from 0 to n """

class PrimeGenerator:
    def __init__(self, number):
        self.number = number

    def prime_generator(self):
        # Check for non-integer
        if not isinstance(self.number, int):
            return "Input should be an integer"

        # Check for negative integer
        if self.number < 0:
            return 'Input should be a positive integer'

        # Check for one
        if self.number == 1:
            return 'One is not prime'

        # Check for zero
        if self.number == 0:
            return 'Zero is not prime'
        
        primes_list = []
        
        # Add a number to a list if it is a prime number and return the list
        return [integer for integer in range(2, self.number + 1) if self.is_prime(integer)]

    """ Takes in an integer and returns true if it is a prime number """
    def is_prime(self, integer):
        for each in range(2, integer):
            if integer % each == 0:
                return False
        return True
