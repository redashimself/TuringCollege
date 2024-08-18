import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_initial_memory(self):
        self.assertEqual(self.calculator.number_in_memory, 0)

    def test_add(self):
        self.assertEqual(self.calculator.add(5), 5)
        self.assertEqual(self.calculator.add(3, 2), 10)
        self.assertEqual(self.calculator.add(3, 2, 5, -2), 18)

    def test_subtract(self):
        self.calculator.add(10)
        self.assertEqual(self.calculator.subtract(3), 7)
        self.assertEqual(self.calculator.subtract(2, 1), 4)
        self.assertEqual(self.calculator.subtract(0, 1, 0, 1), 2)

    def test_multiply(self):
        self.calculator.add(5)
        self.assertEqual(self.calculator.multiply(3), 15)
        self.assertEqual(self.calculator.multiply(2, 2), 60)
        self.assertEqual(self.calculator.multiply(-1, 2.2121212), -132.727272)

    def test_divide(self):
        self.calculator.add(20)
        self.assertEqual(self.calculator.divide(4), 5)
        with self.assertRaises(ValueError):
            self.calculator.divide(0)

    def test_root(self):
        self.calculator.add(16)
        self.assertEqual(self.calculator.root(2), 4)
        self.calculator.add(11)  # memory is now 27
        self.assertEqual(round(self.calculator.root(3), 5), 2.46621)
        with self.assertRaises(ValueError):
            self.calculator.root(0)
        self.calculator.add(-8)
        with self.assertRaises(ValueError):
            self.calculator.root(2)

    def test_reset(self):
        self.calculator.add(10)
        self.assertEqual(self.calculator.reset(), 0)
        self.assertEqual(self.calculator.number_in_memory, 0)

    def test_memory_property(self):
        self.calculator.number_in_memory = 15
        self.assertEqual(self.calculator.number_in_memory, 15)


if __name__ == '__main__':
    unittest.main()
