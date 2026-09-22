"""
This file defines some custom exception types for use in this lab
These 3 exception types have been imported in main.py, so you can 
raise and handle them just like any other exception.
You can mostly ignore this file for now - it'll make more sense after
we cover classes and objects.
"""


class TextFormatException(Exception):
    pass

class MissingValueException(Exception):
    pass

class MeasurementUnitException(Exception):
    pass
