import unittest
import calculator

class Testing(unittest.TestCase):
    
##Addition
    def test_addition(self):    ##This test will pass
        result = calculator.addition(5, 5)
        self.assertEqual(result, 10)

    def test_addition2(self):    ##This test will fail
        result = calculator.addition(5, 10)
        self.assertEqual(result, 7)

##Subtraction
    def test_sub(self):         ##This test will pass
        result = calculator.sub(10, 5)
        self.assertEqual(result, 5)

    def test_sub2(self):         ##This test will fail
        result = calculator.sub(10, 5)
        self.assertEqual(result, 10)

##Division
    def test_divide(self):      ##This test will pass
        result = calculator.divide(10, 5)
        self.assertEqual(result, 2)

    def test_divide2(self):      ##This test will fail
        result = calculator.divide(10, 0)
        self.assertEqual(result, 2)

##Multiplication
    def test_multiply(self):    ##This test will pass
        result = calculator.multiply(2, 5)
        self.assertEqual(result, 10)

    def test_multiply2(self):    ##This test will fail
        result = calculator.multiply(5, 5)
        self.assertEqual(result, 65)