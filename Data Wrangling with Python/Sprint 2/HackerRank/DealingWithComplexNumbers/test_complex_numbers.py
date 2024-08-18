import unittest
from complex_numbers import Complex


class TestComplex(unittest.TestCase):
    def setUp(self):
        self.c1 = Complex(2, 1)
        self.c2 = Complex(5, 6)

    def test_add(self):
        result = self.c1 + self.c2
        self.assertEqual(str(result), "7.00+7.00i")

    def test_sub(self):
        result = self.c1 - self.c2
        self.assertEqual(str(result), "-3.00-5.00i")

    def test_mul(self):
        result = self.c1 * self.c2
        self.assertEqual(str(result), "4.00+17.00i")

    def test_truediv(self):
        result = self.c1 / self.c2
        self.assertEqual(str(result), "0.26-0.11i")

    def test_mod(self):
        self.assertEqual(str(self.c1.mod()), "2.24+0.00i")
        self.assertEqual(str(self.c2.mod()), "7.81+0.00i")


if __name__ == '__main__':
    unittest.main()
