import unittest
from Calc import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = Calculator()
        
    def test_calc_sum(self):
        self.assertEqual(self.calculator.calc_sum(4, 7), 11)
        
    def test_calc_minus(self):
        self.assertEqual(self.calculator.calc_minus(10, 0), 10)
    
    def test_calc_multiply(self):
        self.assertEqual(self.calculator.calc_multiply(5, 5), 25)
        
    def test_calc_division(self):
        self.assertEqual(self.calculator.calc_division(10, 5), 2)
        
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calc_division(10, 0)
    
    def test_calc_sqrt(self):
        self.assertEqual(self.calculator.calc_sqrt(4), 2)
        
    def test_calc_pow(self):
        self.assertEqual(self.calculator.calc_pow(5, 2), 25)
    
    
if __name__ == '__main__':
    unittest.main()