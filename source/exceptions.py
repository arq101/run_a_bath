# -*- coding: utf-8 -*-

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InvalidOption(Error):
    pass


class ValueTooLow(Error):
    pass


class ValueTooHigh(Error):
    pass
