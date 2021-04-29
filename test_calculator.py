import unittest
import calculator

class Testing(unittest.TestCase):
    def test_addition(self):
        result = calculator.addition(5, 5)
        self.assertEqual(result, 10)

    