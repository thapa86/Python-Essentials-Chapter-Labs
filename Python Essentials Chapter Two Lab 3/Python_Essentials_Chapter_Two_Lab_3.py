
#Chapter 2 Lab 1 - The print() function
# Using the print() function to print the line "Hello, Python!" and "Anil"
print("Hello, Python!")
print("Anil \n")

# Chapter 2 Lab 2 - The print() function using separator and end keywords
# Using sep and end keyword arguments to achieve the expected output
print("Programming","Essentials","in", sep="***", end="...")
print("Python \n")


# Chapter 2 Lab 3 - Formatting the output 
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

# Chapter 2 Lab 4 - Python literals - Strings
# Writing a one-line piece of code using the print() function as well as the newline and escape characters
print("I'm\" \n\"\"learning\"\" \n\"\"\"Python\"\"\"\n")

# Chapter 2 Lab 5 - Variables
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

# Chapter 2 Lab 6 - A simple Converter
# Defining the variables and assigning values to them
kilometers = 12.25
miles = 7.38

# As 1 mile equals 1.6 km, multiplied by 1.6 to get km and division by 1.6 to get miles
miles_to_kilometers = miles*1.6
kilometers_to_miles = kilometers/1.6

# Print function where there are some strings and some variable. The result of the converter is rounded to 2 decimal places
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles","\n")

# Chapter 2 Lab 7 Operators and Expressions
#Using the first value of 0
x =  0
x = float(x)

# Code which would calculate the value of y as derived from the algebraic expression, " 3x^3 - 2x^2 + 3x - 1"
y = 3*x**3-2*x**2+3*x-1

# Printing the result of y
print("When x = 0")
print("y =", y, "\n")

#Using the second value of 1
x =  1
x = float(x)

# Code which would calculate the value of y as derived from the algebraic expression, " 3x^3 - 2x^2 + 3x - 1"
y = 3*x**3-2*x**2+3*x-1

# Printing the result of y
print("When x = 1")
print("y =", y, "\n")

#Using the third value of -1
x = -1
x = float(x)

# Code which would calculate the value of y as derived from the algebraic expression, " 3x^3 - 2x^2 + 3x - 1"
y = 3*x**3-2*x**2+3*x-1

# Printing the result of y
print("When x = -1")
print("y =", y, "\n")

# Chapter 2 Lab 8 - Comments
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