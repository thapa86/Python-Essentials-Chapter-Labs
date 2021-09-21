
#Prompting users to end a program.
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

# Chapter Three
# Read two numbers and identify the larger of two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Comprehensive way if only one instruction after if or else
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
#largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number1 > number2:
    largest_number = number1

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number1 > number3:
    largest_number = number1

if number2 > number1:
    largest_number = number2

if number2 > number3:
    largest_number = number2

if number3 > number1:
    largest_number = number3

if number3 > number2:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

# Using max() and min() build-in function.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)





