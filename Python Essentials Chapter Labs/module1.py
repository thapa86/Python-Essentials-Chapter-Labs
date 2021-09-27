# *********************************************************************************************************************************************
# Chapter 4.3.1.8 Day of the year: writing and using your own functions
# This lab is about creating a function which takes three arguments(year, month and a day). It returns the corresponding day of the year
# or returns None if any of the arguments is invalid

# Code from LAB 4.3.1.6.
def is_year_leap(year):

# If and elif statement which defines the condition for a year to be a leap year
	if year % 4 != 0: # if the year is not evenly divisible by 4, then it is not a leap year
		return False
	elif year % 100 != 0: #modulus of 100 if returns 0 means exactly divisible by 100. If not exactly divisible, it is a leap year
		return True
	elif year % 400 != 0: # if not evenly divisible by 400, then it is not a leap year
		return False
	else:
		return True # Otherwise, the year is a leap year
# Creates a function which takes two arguments (a year and a month)
def days_in_month(year, month):

	# List for common year months. Each month has 28,30 or 31 days for common year
	days_common_year = [31,28,31,30,31,30,31,31,30,31,30,31] # List of days in months for common year
	
	# List for leap year months. Leap year has 29, 30 and 31 days
	days_leap_year = [31,29,31,30,31,30,31,31,30,31,30,31] # List of days in months for leap year
	
	# Calls is_leap_year function and test if the year entered as parameter is leap year or not
	if is_year_leap(year):
		return days_leap_year[month-1] # If condition true, returns number of days for the month. Month-1 as first element in list start at 0
									   # Uses leap year list for returning number of days

	# else statement to check if not a leap year
	else:
		return days_common_year[month-1] # returns number of days for month specified in parameter as per common_year list

# Function which takes three arguments (a year, a month, and a day of the month)
def day_of_year(year, month, day):

# and returns the corresponding day of the year, 
# or returns None if any of the arguments is invalid.

print(day_of_year(2000, 12, 31))
# Use the previously written and tested functions. Add some test cases to the code. This test is only a beginning.	
