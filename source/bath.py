# -*- coding: utf-8 -*-
import time
import exceptions as exp
from logger import logger


class Bath(object):
    """ Class used to a run a bath.

    """

    fragrances = ['lavender', 'eucalyptus', 'summer_fruits']

    def __init__(self, water_level='1/2', temperature=32, soap=True, scents=[]):
        self.water_level = water_level
        self.temperature = temperature
        self.soap = soap
        self.scents = scents

    def _tap_run_time(self):
        """ Determines the number of minutes the taps will run for, given the bath water level.

        Note: in this exercise 1 second will represent 1 minute.
        Assuming it takes 2 minutes to fill a 1/4 of generic bath tub, and there is no change in water pressure.
        """
        if self.water_level == '1/4':
            return 2
        elif self.water_level == '1/2':
            return 4
        elif self.water_level == '3/4':
            return 6
        else:
            return 8

    def _check_water_level(self):
        """ This particular bath tub can be filled to 4 pre-selected levels.
        """
        if self.water_level not in {'1/4', '1/2', '3/4', 'FULL'}:
            raise exp.InvalidOption("Invalid water level was specified!")

    def _check_temperature(self):
        """ The water temperature must be selected between the acceptable temperature range in degrees Celcius.
        """
        if self.temperature < 15:
            raise exp.ValueTooLow("Dangerously low temperature of {} degrees Celcius!".format(self.temperature))
        elif self.temperature > 40:
            raise exp.ValueTooHigh("Dangerously high temperature of {} degrees Celius!".format(self.temperature))

    def _check_scent_options(self):
        """ Checks if the scents available have been selected.
        """
        if self.scents:
            for scent in self.scents:
                if scent not in self.fragrances:
                    raise exp.InvalidOption("Unknown scent %s specified!" % scent)

    def _prepare_to_run(self):
        """ Verifies all the user supplied arguments are valid.
        """
        self._check_water_level()
        self._check_temperature()
        self._check_scent_options()

    def _open_taps(self):
        """ Once all checks have been completed, runs the water.
        """
        self._prepare_to_run()
        logger.info('Running water & dispenser:')
        logger.info('temp={0}C, water_level={1}, soap_included={2}, scents={3}.'.format(
            self.temperature,
            self.water_level, self.soap,
            'None' if not self.scents else self.scents))

    def _close_taps(self):
        logger.info('Closing taps.')

    def run_bath(self):
        """ Fills the bath tub to the specified level for the given temperature.
        """
        run_time = self._tap_run_time()
        self._open_taps()
        time.sleep(run_time)
        self._close_taps()
