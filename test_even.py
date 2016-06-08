# import the python testing framework
import unittest


# our "unit"
# this is what we are running our test on
def is_even(n):
    return n % 2 == 0


# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run
    def test_two(self):
        self.failUnless(is_even(2))

    def test_three(self):
        self.failIf(is_even(3))

if __name__ == '__main__':
    unittest.main()  # this runs our tests
