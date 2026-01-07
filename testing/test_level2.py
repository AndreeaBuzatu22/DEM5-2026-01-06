import unittest
from calculator import Calculator

class TesdOperations(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator(8,2)

    def test_sum(self):
        sum = self.calc.get_sum()      
        self.assertEqual(sum, 10, 'The Answer was not 10')

    #test difference
    def test_diff(self):
        diff = self.calc.get_diff()
        self.assertEqual(diff, 10, 'The Answer was not 10')


if __name__ =='__main__':
    unittest.main()
