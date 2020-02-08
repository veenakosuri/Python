import unittest

from leap import leap_year, LeapError

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.6.0

@classmethod
def setUpClass (cls):
    pass

@classmethod
def tearDownClass (cls):
    pass

def setUp (self):
    pass

def tearDown (self):
    pass

class LeapTest(unittest.TestCase):
    def test_year_not_divisible_by_4_in_common_year(self):
        self.assertIs(leap_year(2015), False)

    def test_year_divisible_by_2_not_divisible_by_4_in_common_year(self):
        self.assertIs(leap_year(1970), False)

    def test_year_divisible_by_4_not_divisible_by_100_in_leap_year(self):
        self.assertIs(leap_year(1996), True)

    def test_year_divisible_by_4_and_5_is_still_a_leap_year(self):
        self.assertIs(leap_year(1960), True)

    def test_year_divisible_by_100_not_divisible_by_400_in_common_year(self):
        self.assertIs(leap_year(2100), False)

    def test_year_divisible_by_100_but_not_by_3_is_still_not_a_leap_year(self):
        self.assertIs(leap_year(1900), False)

    def test_year_divisible_by_400_in_leap_year(self):
        self.assertIs(leap_year(2000), True)

    def test_year_divisible_by_400_but_not_by_125_is_still_a_leap_year(self):
        self.assertIs(leap_year(2400), True)

    def test_year_divisible_by_200_not_divisible_by_400_in_common_year(self):
        self.assertIs(leap_year(1800), False)

    def test_year_invalid_year_string_value(self):
        self.assertRaises(ValueError, leap_year, 'two zero tow zero')

    def test_year_invalid_year_negative_number(self):
        self.assertRaises(LeapError, leap_year, -2434)

    def test_year_invalid_year_big_number(self):
        self.assertRaises(LeapError, leap_year, 12345)

if __name__ == "__main__":
    unittest.main()
