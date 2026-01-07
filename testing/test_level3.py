import unittest
import pandas as pd
from cleaning_script import calculate_borrow_time

class TesdOperations(unittest.TestCase):
    def setUp(self):
        self.valid_row = pd.Series({
            "checkout_date": pd.Timestamp('2026-01-01'),
            "return_date": pd.Timestamp('2026-01-05')
        })
        self.invalid_row = pd.Series({
            "checkout_date": pd.Timestamp('2026-01-08'),
            "return_date": pd.Timestamp('2026-01-05')
        })

    def test_valid(self):
        dates = calculate_borrow_time(self.valid_row)     
        self.assertEqual(dates, 4 )
    
    def test_invalid(self):
        dates = calculate_borrow_time(self.invalid_row)     
        self.assertEqual(dates, -3 )



if __name__ =='__main__':
    unittest.main()
