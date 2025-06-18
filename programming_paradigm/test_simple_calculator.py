import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5,3), 8)
        self.assertEqual(self.calc.add(-3,3), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3), 2)
        self.assertEqual(self.calc.subtract(-5,3), -8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,6), 30)
        self.assertEqual(self.calc.multiply(5,-6), -30)

    def test_divide(self):
        self.assertEqual(self.calc.divide(15,3), 5)
        self.assertEqual(self.calc.divide(20,5), 4)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10,0))
        self.assertIsNone(self.calc.divide(0,0))
