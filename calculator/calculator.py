#!/usr/bin/env python
# description : This file defines all the calculator related functions.
__author__  = 'Vineel.Vallepu'
__email__   = 'vallepu.vineel@gmail.com'
__version__ = '1.0'
__status__  = 'Test'

# import user defined global enum
from global_definitions import NO_OF_DAYS_IN_MONTH

class Calculator:
    """Calculator class definition"""

    def __init__(self):
        """Constructor"""
        pass

    def get_days_difference(self, startDate, endDate):
        """This function expects start and end date object calculates the difference between them and returns the
        difference in days."""

        daysLeft    = self.get_days_left(startDate)                    # Calculates the days left in start year.
        daysCovered = self.get_days_elapsed(endDate)                   # Calculates the days elapsed in end year.

        if startDate.year == endDate.year:                             # Compare if both start and end year are same.
            if startDate.year%4 == 0:                                  # Check for leap year.
                daysInYears = -366                                     # Deduct 366 days if its a leap year.
            else:
                daysInYears = -365                                     # Deduct 365 days it its non leap year.
        else:
            daysInYears = self.get_mean_year_days(startDate, endDate)  # Total days in mean years.
        return daysLeft+daysCovered+daysInYears                        # Return the difference.

    def get_days_left(self, dateObj):
        """This function expects date object and does calculation of days left in year given including day mentioned.
        Return number of days left in given year."""

        daysLeft = 365                                               # Assign 365 days by default to total days.
        for i in NO_OF_DAYS_IN_MONTH:                                 # Iterate through the months.
            if i[0] < dateObj.month:                                  # Check if given month is less than iterator.
                daysLeft -= i[1]                                     # Deduct the number of days in months left.
        daysLeft -= dateObj.day                                      # Deduct days elapsed including
                                                                      # the day mentioned.
        return daysLeft                                              # Returns the total days left in given year.

    def get_days_elapsed(self, endDate):
        """This function expects date object and does calculation of days elapsed in year given excluding day mentioned.
        Return number of days elapsed in given year."""

        daysElapsed = 0                                              # Assign days_elapsed offset to 0
        for i in NO_OF_DAYS_IN_MONTH:                                 # Iterate through the months.
            if i[0] < endDate.month:                                  # Check if given month is less than iterator.
                daysElapsed += i[1]                                  # Add the number of days in months elapsed.
        if (endDate.year%4) == 0 and endDate.month > 2:               # If leap year and month is Feb and additional day
            daysElapsed += 1
        daysElapsed += endDate.day-1                                 # Add the days elapsed excluding the day defined.
        return daysElapsed                                           # Returns days elapsed in given year.

    def get_mean_year_days(self, startDate, endDate):
        """This function expects start and end date object calculates the days in between those years."""

        daysInYear = 0                                              # Set days in year to 0
        for i in range(startDate.year+1, endDate.year):               # Iterate through the years excluding the defined.
            daysInYear += 365                                       # Add 365 days by default
            if i%4 == 0:                                              # Check if leap year
                daysInYear += 1                                     # Add a day if its a leap year
        return daysInYear                                           # Return the total days in between years given.