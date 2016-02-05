#!/usr/bin/env python
# description : date class file, to create an object and any related functions can be added in here.
__author__  = 'Vineel.Vallepu'
__email__   = 'vallepu.vineel@gmail.com'
__version__ = '1.0'
__status__  = 'Test'

class Date:
    """Date class definition"""

    def __init__(self, date):
        """Constructor of Date Class"""

        self.date = date                            # Assign date string to date variable
        self.day = int(date.split('/')[0])          # set day from date string given
        self.month = int(date.split('/')[1])        # set month from date string given
        self.year = int(date.split('/')[2])         # set year from date string given
