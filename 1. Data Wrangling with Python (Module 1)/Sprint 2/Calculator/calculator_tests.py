import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_initial_memory(self):
        self.assertEqual(self.calculator.number_in_memory, 0)

    def test_add(self):
        self.assertEqual(self.calculator.add(5).number_in_memory, 5)
        self.assertEqual(self.calculator.add(3, 2).number_in_memory, 10)
        self.assertEqual(self.calculator.add(3, 2, 5, -2).number_in_memory, 18)

    def test_subtract(self):
        self.calculator.add(10)
        self.assertEqual(self.calculator.subtract(3).number_in_memory, 7)
        self.assertEqual(self.calculator.subtract(2, 1).number_in_memory, 4)
        self.assertEqual(self.calculator.subtract(0, 1, 0, 1).number_in_memory, 2)

    def test_multiply(self):
        self.calculator.add(5)
        self.assertEqual(self.calculator.multiply(3).number_in_memory, 15)
        self.assertEqual(self.calculator.multiply(2, 2).number_in_memory, 60)
        self.assertAlmostEqual(self.calculator.multiply(-1, 2.2121212).number_in_memory, -132.727272, places=6)

    def test_divide(self):
        self.calculator.add(20)
        self.assertEqual(self.calculator.divide(4).number_in_memory, 5)
        with self.assertRaises(ValueError):
            self.calculator.divide(0)

    def test_root(self):
        # Test square root
        self.calculator.reset()
        self.calculator.add(16)
        self.assertAlmostEqual(self.calculator.root(2).number_in_memory, 4, places=5)

        # Test cube root
        self.calculator.reset()
        self.calculator.add(27)
        self.assertAlmostEqual(self.calculator.root(3).number_in_memory, 3, places=5)

        # Test 0th root
        with self.assertRaises(ValueError):
            self.calculator.root(0)

        # Test even root of negative number
        self.calculator.reset()
        self.calculator.add(-8)
        with self.assertRaises(ValueError):
            self.calculator.root(2)

        # Test odd root of negative number
        self.calculator.reset()
        self.calculator.add(-8)
        self.assertAlmostEqual(self.calculator.root(3).number_in_memory, -2, places=5)

    def test_reset(self):
        self.calculator.add(10)
        self.assertEqual(self.calculator.reset().number_in_memory, 0)
        self.assertEqual(self.calculator.number_in_memory, 0)

    def test_memory_property(self):
        self.calculator.number_in_memory = 15
        self.assertEqual(self.calculator.number_in_memory, 15)

    def test_chained_operations(self):
        result = self.calculator.add(10).multiply(2).subtract(5).divide(3).number_in_memory
        self.assertAlmostEqual(result, 5, places=5)


if __name__ == '__main__':
    unittest.main()
