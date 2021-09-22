# Anil Thapa - Chapter 2 Labs -20210921

#Chapter 2.1.1.6 - The print() function - 20210921
# Using the print() function to print the line "Hello, Python!" and "Anil"
print("Hello, Python!")
print("Anil \n")

# Chapter 2.1.1.18 - The print() function using separator and end keywords
# Using sep and end keyword arguments to achieve the expected output
print("Programming","Essentials","in", sep="***", end="...")
print("Python \n")

# Chapter 2.1.1.19 - Formatting the output 
# Minimizing the number of print() function invocations by inserting the \n sequence into the strings
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n")

# The original code for Single Arrow display
print("Single Arrow")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****\n")

# Making the arrow twice as large but keeping the proportions
print("Doubled Arrow")
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("*****       *****")
print("    *       *")
print("    *       *")
print("    *       *")
print("    *       *")
print("    *       *")
print("    *********\n")

# Duplicating the doubled arrows side by side by using "string" * 2
print("Duplicated Arrows")
print("        *         " * 2)
print("       * *        " * 2)
print("      *   *       " * 2)
print("     *     *      " * 2)
print("    *       *     " * 2)
print("   *         *    " * 2)
print("  *           *   " * 2)
print(" *             *  " * 2)
print("*****       ***** " * 2)
print("    *       *     " * 2)
print("    *       *     " * 2)
print("    *       *     " * 2)
print("    *       *     " * 2)
print("    *       *     " * 2)
print("    *********     " * 2, "\n")

# Chapter 2.2.1.11 - Python literals - Strings
# Writing a one-line piece of code using the print() function as well as the newline and escape characters
print("I'm\" \n\"\"learning\"\" \n\"\"\"Python\"\"\"\n")

# Chapter 2.4.1.7
# Creating the variables and assigning values to each variables
john = 3
mary = 5
adam = 6
total_apples = john+mary+adam

# Print the variables on one line, separated by comma
print(john, mary, adam, sep=",")

# Print the value stored in total_apples to the console
print(total_apples,"\n")

# Experiment with the codes and assigning different values
john = 10
mary = 16.5
adam = 13.2

# Using various arithmetic operations when defining total_apples
total_apples = john*mary/adam+john-mary//adam

# Print a string and an integer together on one line
print("Experiment of code")
print("Total number of apples:", total_apples,"\n")


# Chapter 2.4.1.9 - Variables: A simple Converter
# Defining the variables and assigning values to them
kilometers = 12.25
miles = 7.38

# As 1 mile equals 1.6 km, multiplied by 1.6 to get km and division by 1.6 to get miles
miles_to_kilometers = miles*1.6
kilometers_to_miles = kilometers/1.6

# Print function where there are some strings and some variable. The result of the converter is rounded to 2 decimal places
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles","\n")

# Chapter 2.4.1.10 Operators and Expressions
#Using the first value of 0
x =  0
x = float(x)

# Code which would calculate the value of y as derived from the algebraic expression, " 3x^3 - 2x^2 + 3x - 1"
y = (3*x**3)-(2*x**2)+(3*x-1)

# Printing the result of y
print("When x = 0")
print("y =", y, "\n")


# Chapter 2.5.1.2 - Comments
# This program computes the number of seconds in a given number of hours

# Defining the variables and assigning values to them
number_of_hours = 2
seconds_in_1hour = 3600

# Printing the number of hours
print("Hours: ", number_of_hours) 

# Printing the number of seconds in a given number of hours
print("Seconds in Hours: ", number_of_hours * seconds_in_1hour, "\n") 

# Printing "Goodbye"
print("Goodbye \n")

# This is the end of the program that computes the number of seconds in 2 hour


# Chapter 2.6.1.9 Simple input and output-20210921
# The task of this lab is to complete the code to evalaure four basic arithmetic operations of two variables 'a' and 'b' as per the user input

a = float(input("Enter your first value here: ")) # This allows user to input a value for 'a' which will be converted to float value
b = float(input("Enter your second value here: ")) # This allows user to input a value for 'b' which will be converted to float value

# This function will output the result of addition of 'a' and 'b'
# Use of "\n" will print the outputs in new line
print("\nThe addition of a and b is", a+b)

# This function will output the result of substraction of 'a' and 'b'
print("\nThe substraction of a and b is", a-b)

# This function will output the result of multiplication of 'a' and 'b'
print("\nThe multiplication of a and b is", a*b)

# This function will output the result of division of 'a' and 'b'
print("\nThe division of a and b is", a/b)

# This will print the message "That's all, folks!"
print("\nThat's all, folks! \n")


# Chapter 2.6.1.10 Operators and Expressions-20210921
# This lab is to complete the code to evaluate the expression given

# This will allow user to input value for 'x' and the value will be converted to float value
x = float(input("Enter value for x: "))

# The value of 'y' is calculted using the following expression
y = 1/(x+1/(x+1/(x+(1/x))))

# This will output the value of y calculated from above expression
print("y =", y, "\n")


# Chapter 2.6.1.11 Operators and expressions -20210921
# This lab is about creating a simple code which will evaluate the end time of a period of time

# The following codes will ask the user to enter starting time in pairs of hours and minutes
# It will also ask the user to input the event duration in minutes
hour = int(input("Starting time (hours): ")) # Hours of Start time, eg: 12 for 12:40 Start time
mins = int(input("Starting time (minutes): ")) # Minutes of Start time, eg: 40 for 12:40 Start time
dura = int(input("Event duration (minutes) ")) # This will input the duration of event in minutes

# To calcuate the end time, firstly total minutes is calculated adding hours, minutes and duration
total_minutes = hour * 60 + mins + dura

# Total minutes is divided by 60 to get hour of end time pair
# int() function is used to get integer value for hour of end time pair
# Modulo operator %24 is used to divide the integer end_hour so that we don't get values above 24 
end_hour = int(total_minutes / 60) % 24 # As there is only 24 hours in a day, therefore, %24

# Remainder of total minutes divided by 60 is end_minutes
end_minutes = total_minutes % 60 # The modulo of 60 as there are 60 minutes in an hour

# Print function to output the endtime and use of 'sep' keyword argument to separate output by ':'
print("\nThe end time is", end_hour, end_minutes, sep=":")









