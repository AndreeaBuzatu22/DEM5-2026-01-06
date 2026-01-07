import unittest
from calculator import Calculator

class TesdOperations(unittest.TestCase):
    def test_sum(self):
        calc1 = Calculator(8,2)
        sum = calc1.get_sum()
        print(f"Sum result is: {sum}")
        
        self.assertEqual(calc1.get_sum(), 10, 'The Answer was not 10')

    #test difference
    def test_sum(self):
        calc2 = Calculator(8,2)
        diff = calc2.get_diff()
        print(f"Diff result is: {diff}")
        
        self.assertEqual(calc2.get_diff(), 10, 'The Answer was not 10')


if __name__ =='__main__':
    unittest.main()
