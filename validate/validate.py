#!/usr/bin/env python
# description : This file defines validations for the inputs
__author__  = 'Vineel.Vallepu'
__email__   = 'vallepu.vineel@gmail.com'
__version__ = '1.0'
__status__  = 'Test'

class Validate:
    """Validate class definition"""

    def __init__(self):
        """Constructor"""
        pass

    def validate_date(self, date):
        """This function checks if the date given is a valid one or not."""

        if date.month <= 12:                                            # Check if month is less than 12..ie.December
            if self.validate_day(date) and self.validate_year(date):    # Check if day and year is valid input
                return True
            else:
                return False
        else:
            return False

    def validate_day(self, date):
        """This function checks if day given is valid or not for corresponding month and year."""

        if date.month in [4,6,9,11]:                                    # Check if month is having 30 days calendar
            maxDay = 30                                                 # Set the max day limit to 30
        elif date.month in [1,3,5,7,8,10,12]:                           # Check if month is having 31 days calendar
            maxDay = 31                                                 # Set the max day limit to 31
        else:                                                           # Else, when its Feb
            if (date.year%4) == 0:                                      # Check if leap year
                maxDay = 29                                             # If leap year, set it to 29
            else:
                maxDay = 28                                             # If non leap year, set it to 28
        if date.day <= maxDay:                                          # Verify day given is in less or equal to max.
            return True
        else:
            return False

    def validate_year(self, date):
        """This function checks if year given is within 1900 and 2900 range or not"""

        if date.year in range(1901,3000):                               # Verify if year given is in (1900, 2999) range.
            return True
        else:
            return False

    def validate_date_range(self, startDate, endDate):
        """This function checks if start date is less than end date"""

        if startDate.year < endDate.year:                               # Verifies if start date year is less than end.
            return True
        elif startDate.year == endDate.year:                            # Verifies if both are in same year.
            if startDate.month < endDate.month:                         # Verifies if start month is less than end.
                return True
            elif startDate.month == endDate.month:                      # Verifies if both are in same month.
                if startDate.day < endDate.day:                         # Verifies if start day is less than end.
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False