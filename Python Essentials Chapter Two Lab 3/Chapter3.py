# Chapter 3 Labs - 20210921 Anil Thapa

# Chapter 3.1.1.4 Questions and Answers 
# This lab is about using one of the comparison operators which takes n parameter as input and compares it to 100

n = int(input("\nEnter a number here: ")) # Will prompt user to enter a value which will be stored as integer

# Compare the value of n and will output 'False' if less than 100 but 'True' if equal to or greater than 100
print(n >= 100)


# Chapter 3.1.1.10 Comparison operators and conditional execution - 20210921
# This lab is about writing a program using conditional execution
# It outputs "Spathiphyllum is the best plant ever!" if input matches the string "Spathiphyllum"

# This line will take the name of plant entered by user as string and store it under the variable 'name_of_plants'
name_of_plants = input("\nEnter plant name here: ")

# Checks if the input is equal to "Spathiphyllum" with upper case
if name_of_plants == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!\n") # Print the output if it matches "Spathiphyllum"

# Checks if the input is equal to "spathiphyllum" with lower case
if name_of_plants == "spathiphyllum":
    print("No, I want a big Spathiphyllum!\n") # Print the output if it matches "spathiphyllum"

# Else statement which will compare if input matches either of two above
# If not matched, it will output the message below with the input string
else:
    print("Spathiphyllum! Not "+ name_of_plants +"!\n")


# Chapter 3.1.1.11 Essentials of the if-else statement - 20210921
# This lab is about creating a tax calculator for income more or less than 85,528 Thalers

income = float(input("Enter the annual income: ")) # It will prompt user to enter their income and float value is stored

# If statement which will compare if the income is less than 85528
if income < 85528:
    tax = (18/100 * income) - 556.02 # tax will be calculated using this expression if income is less than 85528

# If statement which will compare if the income is greater than 85528
if income > 85528:
    tax = 14839.2 + (32/100) * (income - 85528) # tax will be calculated using this expression if income is greater than 85528

# If statement which will compare if the tax calculated is greater than 0
if tax > 0:
    tax = round(tax, 0) # Use of round(0) function to round the tax amount to 0 decimal places
    print("The tax is:", tax, "thalers") # Outputs the result with tax value rounded from previous line

# If tax is less than 0, it means no tax at all and will output the following
else:
    print("The tax is: 0.0 thalers")


# Chapter 3.1.1.12 Essentials of the if-elif-else statement - 20210921
# This will identify whether the year entered as input is leap year or common year

year = int(input("\nEnter a year: ")) # int() function which will convert input string to integer

# Compares if the entered year is greater than or equal to 1582
# If within Gregorian calendar period, the following conditions will be executed
if year >= 1582:
    if (year % 4) != 0: # modulus of 4 if returns 0 means exactly divisible by 4
        print("Common year")

    elif (year % 100) != 0: # modulus of 100 if returns 0 means exactly divisible by 100
        print("Leap year")

    elif (year % 400) != 0: # modulus of 400 if returns 0 means exactly divisible by 400
        print("Common year")

# else statement for all other years which do not meet conditions above will be leap year
    else:
        print("Leap year")

# if statement for year before the introduction of the Gregorian calendar period
if year < 1582:
    print("Not within the Gregorian calendar period")
