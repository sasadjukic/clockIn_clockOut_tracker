
import unittest
import datetime
from employee_clockIn_clockOut import convert_time_to_decimal, find_decimal_shift_length, configure_time

class TestEmployee(unittest.TestCase):

    def setUp(self):

        self.time = datetime.datetime(year=2022, month=12, day=10, hour=9, minute=15, second=31)

    def test_decimal_time(self):

        time = self.time
        self.assertEqual(convert_time_to_decimal(time), 555)

    def test_shift_length(self):

        time_in = 555
        time_out = 825
        self.assertEqual(find_decimal_shift_length(time_out, time_in), 4.5)

    def test_configure_time(self):

        time = self.time
        self.assertEqual(configure_time(time), '2022-12-10 09:15:31')


if __name__ == '__main__':
    unittest.main()