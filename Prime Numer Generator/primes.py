""" Class that generates prime numbers from 0 to n """

class PrimeGenerator:
    def __init__(self, number):
        self.number = number

    def prime_generator(self):
        # Check for non-integer
        if not isinstance(self.number, int):
            return "Input should be an integer"
        
        primes_list = []
        
        # Add the number to the list if it is a prime number
        for integer in range(2, self.number + 1):
            if self.is_prime(integer):
                primes_list.append(integer)

        return primes_list

    """ Takes in an integer and returns true if it is a prime number """
    def is_prime(self, integer):
        for each in range(2, integer):
            if integer % each == 0:
                return False
