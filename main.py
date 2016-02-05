#!/usr/bin/env python
# description : main file that needs to be run to test this calculator
__author__  = 'Vineel.Vallepu'
__email__   = 'vallepu.vineel@gmail.com'
__version__ = '1.0'
__status__  = 'Test'

# import system defined modules
import sys
from datetime import datetime

#import user defined modules
from validate.validate import Validate as validate
from calculator.calculator import Calculator
from Date.date import Date


def read_input(a):
    """This function expects command line input from user and returns valid string object.
    It also raises an exception in case of invalid keyed in data."""

    try:
        dateObj = raw_input("Enter %s in (DD/MM/YYY) format:"%a)        # Read in data from command line
        datetime.strptime(dateObj,"%d/%m/%Y")                           # Validate string input in date expected format
        return dateObj                                                  # Return valid date string object
    except ValueError:
        print "Invalid %s format keyed in, please try again...."%a      # Exception print informing user about the same
        sys.exit()                                                      # Exit the programme

def create_date_obj(dateString, stringText):
    """This function expects string object and returns a valid user defined date class object.
    It also raises an exception in case of invalid date string format received."""

    try:
        dateObj = Date(dateString)                                      # Create user defined date class object
                                                                        # for date string provided
        if validate.validate_date(validateObj, dateObj):                # Verifies if date object is in defined criteria
                                                                        # (i.e)
            return dateObj                                              # Returns date class object
        else:
            raise ValueError                                            # Raise an exception if criteria doesnt match
    except ValueError:
        print "Invalid %s range keyed in, please try again"%stringText  # Exception print informing user about the same
        sys.exit()                                                      # Exit the programme

def calculate_date_range(startDateObj, endDateObj):
    """This function expects user defined date class object for start and end dates.Returns difference between the same.
    If end date is less than start date, it just calucalte the difference backwards"""

    if validate.validate_date_range(validateObj, startDateObj, endDateObj):  # Validates if start date is less than end date.
        return calObj.get_days_difference(startDateObj, endDateObj)
    else:
        return calObj.get_days_difference(endDateObj, startDateObj)

if __name__ == "__main__":

    validateObj = validate()                                            # Create Validate class object
    calObj = Calculator()                                               # Create Calculator class object

    startDateString = read_input("start date")                          # Call read_input to read start date in
                                                                        # (DD/MM/YYY) format. ex: 02/06/2001
    startDateObj = create_date_obj(startDateString, "start date")       # Create Date object from the date string

    endDateString = read_input("end date")                              # Call read_input to read end date in
                                                                        # (DD/MM/YYY) format. ex: 22/06/1983
    endDateObj = create_date_obj(endDateString, "end date")             # Create Date object from the date string

    difference = calculate_date_range(startDateObj, endDateObj)         # Call function to validate and calculate
                                                                        # the difference between dates

    print "The Experiment was run for %s days"%str(difference)          # Return Output to user.