## imports
import unittest
import math

## create class
class Calculator(object):

    ## define method for addition
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
    
    ## define method for subtraction
    def subtract(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError

    ## define method for multiplication
    def multiply(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError
            
    ## define method for division
    def divide(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            if y == 0:
                return "NaN"
            else:
                return float(x) / y
        else:
            raise ValueError
			
	## define method for exponent
    def exponent(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            if (x == 0) and (y <= 0):
                return "NaN"
            else:
                return math.pow(x,y)
        else:
            raise ValueError
    
    ## define method for square root
    def squareRoot(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            if x < 0:
                return "NaN"
            elif x == 0:
                return 0
            else:
                return math.sqrt(x)
        else:
            raise ValueError
    
    ## define method for factorial
    def factorial(self, n):
        number_types = (int, long)
        if isinstance(n, number_types):
            if 0 <= n:
                return reduce(lambda x,y:x*y, [1]+range(1,n+1))
            else:
                return "NaN"
        else:       
            raise ValueError
    
    ## define method for ncr
    def ncr(self, n, r):
        number_types = (int, long)
        if isinstance(n, number_types) and isinstance(r, number_types):
            if (r <= n) and (0 <= r):
                return self.factorial(n) / ( self.factorial(r) * self.factorial(n-r) )
            else:
                return "NaN"
        else:        
            raise ValueError
    
    ## define method for npr
    def npr(self, n, r):
        number_types = (int, long)
        if isinstance(n, number_types) and isinstance(r, number_types):
            if (r <= n) and (0 <= r):
                return self.factorial(r) * self.ncr(n,r)
            else:
                return "NaN"
        else:        
            raise ValueError
            
    ## define method for log (base 10)
    def log(self, x):
        number_types = (int, long, float)
        if isinstance(x, number_types):
            if 0 < x:
                return math.log10(x)
            else:
                return "NaN"
        else:        
            raise ValueError

## unittest extends testcase
class TestCalculator(unittest.TestCase):

    def setUp(self):
        ## create an instance of calculator to use throughout
        self.calc = Calculator()

    ## test the calculator functionality
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2,2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2,-2)
        self.assertEqual(0, result)
    
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(2,2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2,-4)
        self.assertEqual(6, result)
        
    def test_calculator_multiply_method_returns_correct_result(self):
        #result = self.calc.multiply(2,2)
        #self.assertEqual(4, result)
        self.assertEqual(4, self.calc.multiply(2,2))
        result = self.calc.multiply(2,4)
        self.assertEqual(8, result)
        result = self.calc.multiply(2,-4)
        self.assertEqual(-8, result)
        result = self.calc.multiply(3,0)
        self.assertEqual(0, result)
        
    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide(4,2)
        self.assertEqual(2, result)
        result = self.calc.divide(-6,2)
        self.assertEqual(-3, result)
        result = self.calc.divide(2,0)
        self.assertEqual("NaN", result)
        
    def test_calculator_exponent_method_returns_correct_result(self):
        result = self.calc.exponent(1,1)
        self.assertEqual(1, result)
        result = self.calc.exponent(2,3)
        self.assertEqual(8, result)
        result = self.calc.exponent(2,-2)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(0,7)
        self.assertEqual(0, result)
        result = self.calc.exponent(0,-5)
        self.assertEqual("NaN", result)
        
    ## test the square root functionality
    def test_square_root_method_returns_correct_result(self):
        result = self.calc.squareRoot(0)
        self.assertEqual(0, result)
        result = self.calc.squareRoot(25)
        self.assertEqual(5, result)
        result = self.calc.squareRoot(-3)
        self.assertEqual("NaN", result)
    
    ## test the factorial functionality
    def test_factorial_method_returns_correct_result(self):
        result = self.calc.factorial(0)
        self.assertEqual(1, result)
        result = self.calc.factorial(5)
        self.assertEqual(120, result)
        result = self.calc.factorial(-7)
        self.assertEqual("NaN", result)

    ## test the ncr functionality
    def test_ncr_method_returns_correct_result(self):
        result = self.calc.ncr(7,0)
        self.assertEqual(1, result)
        result = self.calc.ncr(12,5)
        self.assertEqual(792, result)
        result = self.calc.ncr(-3,2)
        self.assertEqual("NaN", result)
        result = self.calc.ncr(3,-2)
        self.assertEqual("NaN", result)
    
    ## test the npr functionality
    def test_npr_method_returns_correct_result(self):
        result = self.calc.npr(7,0)
        self.assertEqual(1, result)
        result = self.calc.npr(12,5)
        self.assertEqual(95040, result)
        result = self.calc.npr(-3,2)
        self.assertEqual("NaN", result)
        result = self.calc.npr(3,-2)
        self.assertEqual("NaN", result)
    
    ## test the log functionality
    def test_log_method_returns_correct_result(self):
        result = self.calc.log(100)
        self.assertEqual(2, result)
        result = round(self.calc.log(85.2), 2)
        self.assertEqual(1.93, result)
        result = self.calc.log(-3.2)
        self.assertEqual("NaN", result)
    
    ## method to test if strings are input then throws an error
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        self.assertRaises(ValueError, self.calc.subtract, 'two', 'three')
        self.assertRaises(ValueError, self.calc.multiply, 'two', 'three')
        self.assertRaises(ValueError, self.calc.divide, 'two', 'three')
        self.assertRaises(ValueError, self.calc.exponent, 'two', 'three')
        self.assertRaises(ValueError, self.calc.ncr, 'two', 'three')
        self.assertRaises(ValueError, self.calc.npr, 'two', 'three')
       
    ## method to test if x is a string then throws an error
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
        self.assertRaises(ValueError, self.calc.subtract, 'two', 3)
        self.assertRaises(ValueError, self.calc.multiply, 'two', 3)
        self.assertRaises(ValueError, self.calc.divide, 'two', 3)
        self.assertRaises(ValueError, self.calc.exponent, 'two', 3)
        self.assertRaises(ValueError, self.calc.ncr, 'two', 3)
        self.assertRaises(ValueError, self.calc.npr, 'two', 3)
    
    ## method to test if y is a string then throws an error
    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
        self.assertRaises(ValueError, self.calc.subtract, 2, 'three')
        self.assertRaises(ValueError, self.calc.multiply, 2, 'three')
        self.assertRaises(ValueError, self.calc.divide, 2, 'three')
        self.assertRaises(ValueError, self.calc.exponent, 2, 'three')
        self.assertRaises(ValueError, self.calc.ncr, 2, 'three')
        self.assertRaises(ValueError, self.calc.npr, 2, 'three')
        
    ## method to test if string is input then throws an error
    def test_factorial_returns_error_message_if_arg_is_a_string(self):
        self.assertRaises(ValueError, self.calc.factorial, "oops")
        self.assertRaises(ValueError, self.calc.squareRoot, "oh no")
        self.assertRaises(ValueError, self.calc.squareRoot, "hells bells")
    
    ## method to test if non-integer is input then throws an error
    def test_factorial_returns_error_message_if_arg_is_non_integer(self):
        self.assertRaises(ValueError, self.calc.ncr, 8.9, 7)
        self.assertRaises(ValueError, self.calc.npr, 9.8, 6)


## find every class that extends unittest.testcase and run it
## run any function that begins with test_
if __name__ == '__main__':
    unittest.main()
