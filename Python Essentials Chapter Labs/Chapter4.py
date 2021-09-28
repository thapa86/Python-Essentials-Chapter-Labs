# Date created: 27 September 2021
# Created by: Anil Thapa
# This file consists of all labs from Chapter 4 of Python Essentials module

# ********************************************************************************************************************************
# Chapter 4.3.1.6 A leap year: writing your own functions
# This lab is about using user-defined functions which takes on argument as year and returns True
# if the year is a leap year or False otherwise

# Creating a function which will take year as parameter
def is_year_leap(year):
	if year < 1583:
		return None
# If and elif statement which defines the condition for a year to be a leap year
	if year % 4 != 0: # if the year is not evenly divisible by 4, then it is not a leap year
		return False
	elif year % 100 != 0: #modulus of 100 if returns 0 means exactly divisible by 100. If not exactly divisible, it is a leap year
		return True
	elif year % 400 != 0: # if not evenly divisible by 400, then it is not a leap year
		return False
	else:
		return True # Otherwise, the year is a leap year

test_data = [1900, 2000, 2016, 1987] # Test data provided

#Take the year from test_data above as argument for the is_year_leap function and returns True if leap year or False if not
print(is_year_leap(1900))
print(is_year_leap(2000))
print(is_year_leap(2016))
print(is_year_leap(1987))

test_results = [False, True, True, False] # Expected test results

for i in range(len(test_data)): # for loop which will iterate acording to the range defined by length of test_data list
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


# *********************************************************************************************************************************************
# Chapter 4.3.1.7 How many days: Writing and Using your own functions
# This lab is about a function which takes two arguments, a year and a month and returns the number of days for thegiven month/year pair

# Creates a function which takes one argument(year) and returns True if leap year or False if not a leap year
def is_year_leap(year):

# Code from LAB 4.3.1.6.
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
	
# Print the number of days in month specified for year
print(days_in_month(1900,2))
print(days_in_month(2000,2))
print(days_in_month(2016,1))
print(days_in_month(1987,11))
print()

# Testing code to test if the output from the function matches the test result specified.
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

print()

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
	if year < 1583: # Validates the year is after the Gregorian Calendar was introduced
		print("Not valid year")
		return None
	if month <= 0: # Validates the month is not entered as '0'
		print("Not valid month")
		return None
	if month > 12: # Validates the month is not entered greater than '12'
		print("Not valid month")
		return None
	if day <= 0 : # Validates the day is not entered as '0'
		print("Not valid day")
		return None
	if day > 31: # Validates the day is not entered greater than '31'
		print("Not valid day")
		return None

	# The Gregorian calendar only started in 1582. So, for taking 1583 as the start year, following days calculated
	days = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"]
	
	leap_years = [] # Store all the leap years
	days_leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
	days_common_year = [31,28,31,30,31,30,31,31,30,31,30,31]
	days_in_selected_year = []
		
	# Year 1, month 1 and day 1 started at saturday
	# for loop to calculate number of leap years
	for i in range(1583,year):
		if is_year_leap(i):
			leap_years.append(i)
			i += 1
	print()
	
	# print(len(leap_years))

	# Calculate the total number of days in leap year before the year parameter
	total_days_in_leap_year = len(leap_years) * 366

	# Calculate the total number of days in common year before the year parameter
	total_days_in_common_year = (year - len(leap_years)) * 365

	# Calculate the number of days in given year parameter
	if is_year_leap(year):
		for j in range(0, int(month)):
			days_in_selected_year.append(days_leap_year[j])
			j +=1
		print()	
		#print((days_leap_year[month-1]))
		#print(days_in_selected_year)

	# Calculate total days in selected year
	total_days_in_selected_year = sum(days_in_selected_year)
	#print(total_days_in_selected_year)

	# Calculate the total days altogether
	total_days_altogether = total_days_in_leap_year + total_days_in_common_year + total_days_in_selected_year
	#print(total_days_altogether)

	# As there is 7 days in a week, modulus of 7 gives the position of the day in days list 
	position_of_day = total_days_altogether % 7
	#print(position_of_day)

	# Finally, the day in that particular year and month
	particular_day = days[position_of_day - 1]
	return(particular_day)

print("\nThe day of the selected year is:")
print(day_of_year(2021,12, 0)) # This will take the parameters for the function and invoke the function
print()

# **********************************************************************************************************************************
# Chapter 4.3.1.9 Prime numbers - how to find them
# This lab is about checking whether a number is prime or not

#The function is defined which is called 'is_prime' and takes one argument to check the number
def is_prime(num):

    if num == 2: # Checks if '2' is passed as the argument and returns True as it is a prime number
        return True

    # As any whole number above 1 and below or upto square root of the number if divides evenly, then it cannot be a prime number
    for i in range(2, num): # As we want to include the square root of a number, we added +1 at the end range 
        
        if num % i == 0: # if any number divided by its subsequent number has '0' as remainder, it is a prime number
            return False #return True if the argument is prime number

        elif num % (num**0.5) == 0: # Any whole number divided by its square root, it returns '0' remainder, then it is a prime number
            return False #return True if the argument is prime number

        else:
            return True

# the range of values for i is from 1 to 19, excluding 20
for i in range(1,20):
    if is_prime(i +1): # for any values of i, 1 will be added and passed as argument to the function def is_prime(num)
        print(i + 1, end=" ") # Print the results with all prime number from range of 2 to 20, excluding 20
print()


# **************************************************************************************************************************************
# Chapter 4.3.1.10 Converting fuel consumption
# This lab is about converting fuel consumption in Europe and the USA

# Creating the function which has a single parameter of 'litres'
def liters_100km_to_miles_gallon(litres):
    
    conversion_to_miles_per_gallon = (3.785411784 * 100000)/(litres * 1609.344) # 1 ltr = 1/3.785411784 gallon and 1 miles = 1.609344 km
    
    return conversion_to_miles_per_gallon # returns the value calculated as conversion from above step

# takes 3.9 as argument and displays the converted result in miles per gallon
print("\n",liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))

# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres
# Litres to gallon
    #1 ltr = 1/3.785411784 gallon
# Gallon to litres
    #1 gallon = 3.785411784 litres
# Miles to km
    #1 miles = 1.609344 km
# Km to miles
    #1 km = 1/1.609344 km

# Creating a function which takes miles as argument and convert it into liters per 100 km
def miles_gallon_to_liters_100km(miles):

    conversion_to_liters_per_100km = (3.785411784 * 100)/(miles * 1.609344) # 1 ltr = 1/3.785411784 gallon and 1 miles = 1.609344 km
    
    return conversion_to_liters_per_100km # returns the value calculated as conversion from above step

# takes 3.9 as argument and displays the converted result in miles per gallon
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))