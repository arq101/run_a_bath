# -*- coding: utf-8 -*-
import unittest
from mock import patch

from source import bath
from source import exceptions as exp


class TestBath(unittest.TestCase):
    """ Test methods used to run a bath.
    """

    def test_tap_run_time(self):
        """ Test if the given water level is an acceptable level.

        Expects water_level argument to be: 1/4, 1/2, 3/4 and FULL.
        And returns the time in seconds: 2, 4, 6, 8 respectfully.
        """
        bath_obj_1 = bath.Bath(water_level='1/4')
        bath_obj_2 = bath.Bath(water_level='1/2')
        bath_obj_3 = bath.Bath(water_level='3/4')
        bath_obj_4 = bath.Bath(water_level='FULL')
        self.assertEqual(bath_obj_1._tap_run_time(), 2)
        self.assertEqual(bath_obj_2._tap_run_time(), 4)
        self.assertEqual(bath_obj_3._tap_run_time(), 6)
        self.assertEqual(bath_obj_4._tap_run_time(), 8)

    def test_check_water_level_with_invalid_option(self):
        """ Test for an invalid water_level option.

        Expect to get an exception.
        """
        bath_obj = bath.Bath(water_level='1/5')
        with self.assertRaises(exp.InvalidOption):
            bath_obj._check_water_level()

        bath_obj = bath.Bath(water_level='HALF')
        with self.assertRaises(exp.InvalidOption):
            bath_obj._check_water_level()

    def test_check_temperature_with_invalid_temperature(self):
        """ Test if a temperature is given below or above the acceptable temp range.

        Expect to get an exception.
        """
        bath_obj = bath.Bath(temperature=14)
        with self.assertRaises(exp.ValueTooLow):
            bath_obj._check_temperature()

        bath_obj = bath.Bath(temperature=41)
        with self.assertRaises(exp.ValueTooHigh):
            bath_obj._check_temperature()

    def test_check_scent_options(self):
        """ Test if an unspecified scent option is given, ie one that does not exist in bath.Bath.fragrances list.

        Expect to get an exception.
        """
        bath_obj = bath.Bath(scents=['lavender', 'onion'])
        with self.assertRaises(exp.InvalidOption):
            bath_obj._check_scent_options()

    @patch('source.bath.logger')
    def test_open_taps(self, mock_logging):
        """ Tests log messages were written to the logger.
        """
        bath_obj = bath.Bath()
        bath_obj._open_taps()
        self.assertTrue(mock_logging.info.called)
        self.assertEqual(mock_logging.info.call_count, 2)

    @patch('source.bath.logger')
    def test_close_taps(self, mock_logging):
        """ Tests log message was written to the logger.
        """
        bath_obj = bath.Bath()
        bath_obj._close_taps()
        self.assertTrue(mock_logging.info.called)
        self.assertEqual(mock_logging.info.call_count, 1)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
