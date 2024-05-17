import unittest
from sympy import symbols
from main import PolynomialProcessor

class TestPolynomialProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = PolynomialProcessor()

    def test_example_1(self):
        a = self.processor.x**3 + 6*self.processor.x**2 + 11*self.processor.x + 6
        b = self.processor.x**3 + 7*self.processor.x**2 + 14*self.processor.x + 8
        gcd, _, _ = self.processor.extended_euclidean_algorithm(a, b)
        self.assertEqual(str(gcd), 'Poly(-x**2 - 3*x - 2, x, domain=\'ZZ\')')

    def test_example_2(self):
        a = self.processor.x**2 + 3*self.processor.x + 2
        b = self.processor.x**2 + 4*self.processor.x + 4
        gcd, _, _ = self.processor.extended_euclidean_algorithm(a, b)
        self.assertEqual(str(gcd), 'Poly(-x - 2, x, domain=\'ZZ\')')

if __name__ == '__main__':
    unittest.main()
