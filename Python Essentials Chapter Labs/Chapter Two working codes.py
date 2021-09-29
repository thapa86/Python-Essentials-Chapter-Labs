#Chapter 2 Labs codes

print("The itsy bitsy spider\nclimbed up the waterspout.")

# The output will be
# The itsy bitsy spider
# climbed up the waterspout.

# Print the octal number
print(00123)

# Print the hexadecimal number
print(0x123)

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

#Chapter three Key takeaways
x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.

# Chapter three elif
x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")

# Nested conditional statements
x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")


# Chapter 3 Loops
# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# Counter loops
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#Second option
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#FOR loops

for i in range(10):
    print("The value of i is currently", i)

for i in range(2, 8):
    print("The value of i is currently", i)

#Power of three
power = 1
for expo in range(16):
    print("3 to the power of", expo, "is", power)
    power *= 3

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

# The break and continue statements

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


#for loop to count from 0 to 10 and print odd numbers
for i in range(0, 11):
    if i % 2 != 0:
        print(i)

#while loop that counts from 0 to 10 and prints odd numbers
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

# for and break statement that stops at @ character and displays word before it

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

#Program with for and continue loop to iterate over a string of digits
#and replace each 0 with x and print the modified string to the screen

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

# Output of the following code - 4,3,2,0
n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

# To output -1 0 1 2 3
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

c0 = int(input("\nEnter any non-negative and non-zero integer number: ")) # Prompt user to enter any non-negative and non-zero integer number
step = 0

# While loop which will execute if value of 'c0' is not equal to 1
while c0 !=1:
    if c0%2 ==0: # any number divided by modulus of 2 if returns 0, then its even number
        c0=c0/2
    elif c0%2 != 0: # any number divided by modulus of 2 if returns 1, then its odd number
        c0 = 3 * c0 + 1
    step +=1 # increment of +1 for all iterations

    print(int(c0)) # Print the intermediate values of c0. int() functions converts the float value to integer
    
else:
    print("\nsteps =", step) # Prints the number of steps taken to achieve the goal


#Chapter three Lists

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers)  # Printing current list content.

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

# Adding items to the list using append and insert method
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)


#List methods using for loop and append method
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

# List methods using for loop and insert method
# Using insert will list number in opposite direction to append

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)


# Calculating the total values of the list

my_list = [1,2,3,4,5]
total = 0

for i in my_list:
    total = total +i

print(total)

# Reversing values using for loop

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

#This will add numbers from lst and create another lst_2 and put all added values of each loop
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

# Bubble Algorithm
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

#Interactive version of the Bubble sort algorithm

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

#Lists more details
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

# Slicing method 
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

# List - Finding the index position of a number in the list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

# To find the number of hits in a lottery
chosen_number = [3,7,11,42,34,49]
lottery_number = [5,11,9,42,3,49]

hits = 0

for number in chosen_number:
    if number in lottery_number:
        hits+=1

print(hits)


#Two-dimensional arrays - Chess board
EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)


# Lists in advanced applications
# To calcuate the average temperature during noon in a month
temps = [[0.0 for h in range(24)] for d in range(31)] # This will create [[0,0,0,0,0..], [0,0,0,0,0,...],[...]]
#
# The matrix is magically updated here.
#

total = 0.0
highest = -100

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

for day in temps:
    for temps in day:
        if temps > highest:
            highest = temp
print("The highest temperature was:" highest)

# to print in like array
for i in temps:
    print(days,i)
    days = days +i

# Three dimensional Advanced list
#eg: finding free rooms in three buildings with 15 floors and 20 rooms in each floor

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
print(rooms)

#To book a room
rooms[2][14][1] = True

#To cancel a room
rooms[0][0][3] = False 

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
print(vacancy)

# Multidimensional list
# It consists of "expression", "for in list" and "if conditional"
board = [["empty" for i in range(8)] for j in range(8)]
board[0][0] = [[1],[2],[3]]
print(board[0][0][2])

# Using for loop to create the same 8 * 8 board
board = []

for i in range(8):
    row = ["Empty" for i in range(8)]
    board.append(row)

#is same as compact form
board = [["Empty" for i in range(8)] for j in range(8)]

# To identify the list, in board[0][2], [0] refers to the row and [2] refers to the column.

#Chapter 4 -Defining functions
#built-in, pre-installed modules, user-defined functions
def function_name():
    function_body

def message(): # Defining a function
    print("Enter a value: ") # body of the function

def message():
    print("Enter a value: ")

message() # calling the function
a = int(input())
message()
b = int(input())
message()
c = int(input())

#Parameterized functions
def message(number):
    print("Enter a number:", number)

message(1)

#This will output "Enter a number: 1"

#Two arguments required for two parameters used within the function
def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")

#The output will be 
#Enter telephone number 11
#Enter price number 5
#Enter number number number

#Positional argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

#Argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


# Mixing both positional and argument
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

    adding(1,2,3)
#The output will be 1+2+3 =6

#or
adding(c=1, b=3, c=1)
#The output will be 2+3+1 =6

#or
adding(3, c=1, b=2)
#The output will be 3+2+1 = 6

# Parametrized functions
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Call the function here.
introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")

# The output will be
# Hello, my name is James Doe
#Hello, my name is Henry Smith
#Hello, my name is William Smith

#Example of three-parameter function
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")

address(s, c, p_c)

#This is wrong example, positional argument must not follow keyword arguments
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error

# Returning a result from a function

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes: #if not True, will terminate the function
        return
    
    print("Happy New Year!")

    happy_new_year(True)
    #will output: 
    #Three...
    #Two...
    #One...
    #Happy New Year!

# def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")

#This will output
#This lesson is interesting!
#'Boredom Mode' ON. # From the function, return is ignored in this instance
#This lesson is boring...

# Returning a result from a function
def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(4))
print(strange_function(1))

#The output will be:
#True
#None

# Lists and functions
def list_sum(lst)
    s = 0

    for element in lst:
        s+=element

    return s

print("The sum of the list is:", list_sum([5,4,3]))
print(list_sum([5, 4, 3]))

# The output
# The sum of the list is: 12

def strange_list_fun(n): #n=5
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i) # As the value is in reverse order, use insert method with 0 placeholder
    
    return strange_list

print(strange_list_fun(5)) # invokes the function and passes '5' to the function above

#The output will be
#[4,3,2,1,0]

# Scopes in python

def my_function(): 
    print("Do I know that variable?", var) 

var = 1 # Outside the function
my_function() 
print(var) 

# Output will be 
# Do I know that variable?1
# 1

def my_function():  
var = 2 print("Do I know that variable?", var)  

var = 1 # Outside the function 
my_function()  
print(var) 

# The output will be 
# Do I know that variable? 2 
# 1 

#How the functions interacts with its arguments? 

def my_function(n): 
    print("I got", n) 
    n += 1 
    print("I have", n) 

var = 1 # Outside the function
my_function(var) 
print(var) 

# The output will be 
# I got 1 
# I have 2  
# 1 

# Changing the parameter’s value does not propagate outside the function.

# The Global Keyword
# Using this keyword eg global var can modify the variable outside the function 

def my_function(): 
    global var 
    var = 2 
        print("Do I know that variable?", var) 

var = 1 # Outside the function 
my_function() 
print(var) 
# Th output will be 
# Do I know that variable? 2 
# 2

# Scope in lists
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# The output will be
# Print #1: [2, 3]
# Print #2: [2, 3]
# Print #3: [0, 1]
# Print #4: [2, 3]
# Print #5: [2, 3]

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# The output will be
# Print #1: [2, 3]
# Print #2: [2, 3]
# Print #3: [3]
# Print #4: [3]
# Print #5: [3]

# A variable that exists inside a function has a scope inside the function body
def adding(x):
    var = 7
    return x + var

print(adding(4))    # outputs: 11
print(var)    # NameError

var = 2
print(var)    # outputs: 2

# global keyword followed by a variable name makes the variable's scope global

def return_var():
    global var
    var = 5
    return var

print(return_var())    # outputs: 5
print(var)    # outputs: 5


# The output will be 2, 2
a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)

# The output will be 2
# 3
a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)

# The two-parameter function to calculate BMI
# Convert fit and inch to meters.
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

# Convert pounds to kg
def lb_to_kg(lb):
    return lb * 0.45359237

# Calculate BMI
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

# Print the result of the calculation
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

# To check if we can create a triangle with three sides
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# The more compact form
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# To check if the triangle is a right-angle triangle

def is_triangle_right_angled (a,b,c):
    if is_a_triangle(a,b,c):
        return True
    if c**" == a**2 + b**2":
        return True

# The more compact form for checking if it is a triangle
def is_a_triangle(a, b, c): # Needs checking if it is a triangle
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# To check if the triangle is a right-angle triangle

def is_triangle_right_angled(a,b,c):
    if is_a_triangle(a,b,c): # If it is a triangle
        return True
    if c**2 == a**2 + b**2: # Using pythogoras theorem
        return True
    if a**2 == c**2 + b**2:
        return True
    if b**2 == a**2 + c**2:
        return True
    return False # Return False otherwise
    
print(is_triangle_right_angled(5,4,3))

# with user input
# The more compact form
def is_a_triangle(a, b, c): # Needs checking if it is a triangle
    return a + b > c and b + c > a and c + a > b

#print(is_a_triangle(1, 1, 1))
#print(is_a_triangle(1, 1, 3))

# To check if the triangle is a right-angle triangle

def is_triangle_right_angled(a,b,c):
    if is_a_triangle(a,b,c): # If it is a triangle
        return True
    if c**2 == a**2 + b**2: # Using pythogoras theorem
        return True
    if a**2 == c**2 + b**2:
        return True
    if b**2 == a**2 + c**2:
        return True
    return False # Return False otherwise
a = float(input("Enter the first side\'s length: ")) 
b = float(input("Enter the first side\'s length: "))
c = float(input("Enter the first side\'s length: ")) 

print(is_triangle_right_angled(a,b,c))

# Evaluating a triangle's area
def is_a_triangle(a, b, c): # Needs checking if it is a triangle
    return a + b > c and b + c > a and c + a > b

#print(is_a_triangle(1, 1, 1))
#print(is_a_triangle(1, 1, 3))

# To check if the triangle is a right-angle triangle

# Calculate the value of S
def heron_formula(a,b,c):
    s = (a +b +c) / 2
    return (s*(s-a)*(s-b)*(s-c))**0.5

# To calculate the area of the triangle

def area_of_triangle(a,b,c):
    if not is_a_triangle(a,b,c):
        return None
    return heron_formula(a,b,c)

print(area_of_triangle(1,1.,2**.5))

# Factorials Function
# 0! = 1 (yes! it's true)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 ** 3 * 4 * ... * n-1 * n

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1 
    product = 1
    for i in range(2, n+1):
        product = product * i
    return product

#Testing for 1 to 6
for n in range(0, 6): # For loop to select the number from range 1 to 6
    print(n, factorial_function(n))

#(Fibi = Fibi-1 + Fibi-2)
#Here are some of the first Fibonacci numbers:

#fib_1 = 1
#fib_2 = 1
#fib_3 = 1 + 1 = 2
#fib_4 = 1 + 2 = 3
#fib_5 = 2 + 3 = 5
#fib_6 = 3 + 5 = 8
#fib_7 = 5 + 8 = 13

def fibonacci_numbers(n):
    if n <= 2 and n> 0:
        return 1
    sum = 0
    elem_1= elem_2=1
    for i in range(3, n+1):
        sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, sum
    return sum
# Testing using for loop
for n in range(1, 10):
    print("fib_",n,"=", fibonacci_numbers(n))

# Recursion
#In this field, recursion is a technique where a function invokes itself.
#These two cases seem to be the best to illustrate the phenomenon - factorials and Fibonacci numbers. Especially the latter.
#The Fibonacci numbers definition is a clear example of recursion. We already told you that:
#Fibi = Fibi-1 + Fibi-2

def fibonacci_numbers(n):
    if n <= 2 and n> 0:
        return 1
    return fibonacci_numbers(n-1)+fibonacci_numbers(n-2)
    
# Testing using for loop
for n in range(1, 10):
    print("fib_",n,"=", fibonacci_numbers(n))

# Recursion for factorial
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
# Testing using for loop
for n in range(1, 10):
    print("The factor of",n,"=", factorial_function(n))

# Tuple and dictionaries

# To create tuples
empty_tuple = ()

# To create one element tuple
one_element_tuple = (1,) # if only number provided, it will assign it as variable and not tuple
one_element_tuple = 1,

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0]) # Output will be 1
print(my_tuple[-1]) # Output will be 1000
print(my_tuple[1:]) # Output will be (10, 100, 1000)
print(my_tuple[:-2]) # Output will be (1,10)

for elem in my_tuple:
    print(elem)
# Output will be
# 1
# 10
# 100
# 1000

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000) # Concatenate the tuple with 1000 and 10000
t2 = my_tuple * 3 # repeats the values inside tuple for three times

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# Tuple can also appear on the left side of the assignment operator '='
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1 # The values will be swapped

print(t1, t2, t3)

# This will count the number of 2 inside the tuple
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4


# Dictionary is a key-value pairs. Key is the word you are looking for in dictionary
# Value is the word returned by the dictionary
# 3 dictionaries
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"} # keys and values which are both string
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310} # keys are strings but values are integers
# Keys as numbers and values as strings or number - number combination is also possible
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print()

# will print the dictionary. The order may be random as they are not lists and the order
# is not preserved
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
        
print(dictionary["cat"]) # Will print 'chat'   
print(dictionary["Suzy"]) # Will print 22657854310   

# How to use a dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

# Methods and functions
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
print(dictionary.items()) # print as tuple
sorted(dictionary.keys()) # print as list
print(dictionary.values()) # print as list

#Console 
#dict_items([('cat', 'chat'), ('dog', 'chien'), ('horse', 'cheval')])
#dict_values(['chat', 'chien', 'cheval'])
#dict_keys(['cat', 'dog', 'horse'])

# looks for each word in "words" list and if found returns the values from dictionary
# else, will print is not in dictionary
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

# When creating dictionaries, hanging indents can be used to make it more readable and programmer friendly
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

# Example 2:
phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }

# For loop for dictionary (using keys() method)
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys(): #keys method
    print(key, ">", dictionary[key])

    # the output will be
    #horse -> cheval
    #dog -> chien
    #cat -> chat

for key in sorted(dictionary.keys()): # sort() function to sort out the dictionary
    print(key, ">", dictionary[key])

# Using items() to publish key-value pair
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

# Using values() method to just print the values
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)
#Output will be
#cheval
#chein
#chat

# To replace the value for "cat"
dictionary['cat'] = 'minou'

# To replace the value for "cat"
dictionary['man'] = 'erfee'

# To insert an item, use update() method
dictionary.update({"duck":"canard"})

# To remove an item

del dictionary["man"]

# To remove the lst item in a dictionary, you can use the popitem() method
# In Pythone before 3.6.7, method removes the random item from the dictionary

dictionary.popitem()

del pol_eng_dictionary    # removes the dictionary
pol_eng_dictionary.clear()   # removes all the items
# To copy dictionary, use copy() method
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()

# To copy from two dictionaries

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

# To convert tuple into dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)

print(colors_dictionary)

# A program to store students score and calculate average using dictionary and tuple
school_class = {} # create an empty dictionary for the input data; the student's name
                  #is used as a key, while all the associated scores are stored in a tuple
                  #(the tuple may be a dictionary value - that's not a problem at all)

while True: # enter an "infinite" loop (don't worry, it'll break at the right moment)
    name = input("Enter the student's name: ") # read the student's name here;
    if name == '': # if the name is an empty string (), leave the loop;
        break
    
    # ask for one of the student's scores (an integer from the range 0-10)
    score = int(input("Enter the student's score (0-10): "))

    #if the score entered is not within the range from 0 to 10, leave the loop;
    if score not in range(0, 11):
	    break
    
    # if the student's name is already in the dictionary, 
    # lengthen the associated tuple with the new score (note the += operator)
    if name in school_class:
        school_class[name] += (score,)

     #if this is a new student (unknown to the dictionary), create a new entry - 
     #its value is a one-element tuple containing the entered score;
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()): # iterate through the sorted students' names;
    adding = 0 # initialize the data needed to evaluate the average (sum and counter)
    counter = 0 # initialize the data needed to evaluate the average (sum and counter)
    
    # we iterate through the tuple, taking all the subsequent scores and updating the sum,
    # together with the counter;
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter) # evaluate and print the student's name and average score.

my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

#Exceptions
# Two exceptions specified
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 

# The last line represents the default exception
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')