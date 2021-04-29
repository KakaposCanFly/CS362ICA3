##To run, enter 'py test_calculator.py'

import unittest
import calculator

class Testing(unittest.TestCase):
    
##Addition
    def test_addition(self):    ##This test will pass
        self.assertEqual(calculator.addition(5, 5), 10)

    def test_addition2(self):    ##This test will fail
        self.assertEqual(calculator.addition(5, 10), 7)

##Subtraction
    def test_sub(self):         ##This test will pass
        self.assertEqual(calculator.sub(10, 5), 5)

    def test_sub2(self):         ##This test will fail
        self.assertEqual(calculator.sub(10, 5), 10)

##Division
    def test_divide(self):      ##This test will pass
        self.assertEqual(calculator.divide(10, 5), 2)

    def test_divide2(self):      ##This test will fail
        self.assertEqual(calculator.divide(10, 0), 2)

##Multiplication
    def test_multiply(self):    ##This test will pass
        self.assertEqual(calculator.multiply(2, 5), 10)

    def test_multiply2(self):    ##This test will fail
        self.assertEqual(calculator.multiply(5, 5), 65)

##Clean it up a bit!
if __name__ == "__main__":
    unittest.main()