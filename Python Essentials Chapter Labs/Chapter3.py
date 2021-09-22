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


# Chapter 3.2.1.3 Essentials of the while loop - Guess the secret number - 20210922
# This lab is about creating a program which would prompt user to guess the secret number
# If not correctly guessed, the user will be stuck on loop. Otherwise, the loop will stop if guessed correctly

secret_number = 777 # Secret number is hidden in variable

# Use of """(triple quotes) to print in multiple pages
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

entered_number = int(input("Enter the guessed number here: ")) # Integers entered by the user will be stored under this variable

# while loop will continue prompting users until number is guessed correctly
# Guessing secret number will terminate the loop
while entered_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    # prompt user to enter a number if guess is incorrect
    entered_number = int(input("Enter the guessed number here: "))
    # if number guessed correctly, the correct number will be printed out
    if entered_number == secret_number:
        print(entered_number)

print("Well done, muggle! You are free now.\n")


# Chapter 3.2.1.6 Essentails of the for loop -counting mississippily - 20210922
# This code counts mississippily to five and displays the print every 1 second.

# importing the time module
import time

# For loop that counts to five starting with first argument '1' and ending at '5' before the stop parameter of '6'
for count in range(1,6):
    # print the count number and the word "Mississippi".
    print(count,"Mississippi") 
    # sleep() function suspends the execution of each subsequent print() function inside the loop for one second
    time.sleep(1)
    
# Print function with the final message.
print("\nReady or not, here I come!")


# Chapter 3.2.1.9 The break statement - Stuck in a loop - 20210922
# This program uses a while loop and continuously asks the user to enter a word unless the user enters the secret word

secret_exit_word = "chupacabra" # Secret exit word stored in variable named secret_exit_word

# Prompt user to enter the guessed secret word to exit the loop
entered_word = input("\nPlease enter the secret word to exit this loop: ")

# While loop which will keep on prompting the user until the secret word is entered
while entered_word != secret_exit_word:
    entered_word = input("Please enter the secret word to exit this loop: ")
    # If statement to compare if the entered_word matches the secret_exit_word
    if entered_word == secret_exit_word:
        # break will terminate the loop if conditions are true for if statement above
        break 

# Ouput the message if secret word guessed correctly
print("\nYou've successfully left the loop")


# Chapter 3.2.1.10 The continue statement - The Ugly Vowel Eater - 20210922
# This lab is about creating a vowel eater which removes vowels from user word and display without vowel

user_word = input("\nPlease enter your word here: ") # Prompt user to enter the word and store the word as strings in user_word variable

user_word = user_word.upper() # Converts the user to to upper case

# For loop to check if the user_word has any letters that match vowels
for letter in user_word:
    #if statement to check if the condition is true
    if letter == "A":
        continue # Continue will skip to next statement
    elif letter == "E":
        continue
    elif letter =="I":
        continue
    elif letter =="O":
        continue
    elif letter =="U":
        continue
    else:
        print(letter) # will output the letters stripping all vowels from user_word


# Chapter 3.2.1.11 The continue statement - The Pretty Vowel Eater - 20210922
# This lab is about redesigning the ugly vowel eater and create a better version

word_without_vowels = ""

user_word = input("\nPlease enter your word here: ") # Prompt user to enter the word and store the word as strings in user_word variable

user_word = user_word.upper() # Converts the user to to upper case

# For loop to check if the user_word has any letters that match vowels
for letter in user_word:
    #if statement to check if the condition is true
    if letter == "A":
        continue # Continue will skip to next statement
    elif letter == "E":
        continue
    elif letter =="I":
        continue
    elif letter =="O":
        continue
    elif letter =="U":
        continue
    # else statement will be executed if letters from user_word does not contain vowels
    else:
        word_without_vowels += letter # This will concatenate the letter string from each iteration of the loop

print(word_without_vowels,"\n") # will output the letters stripping all vowels from user_word


# Chapter 3.2.1.14 Essentails of the while loop-20210922
# This lab is about a pyramid-shaped wall. The program should read the number of blocks the builders have and output the height of the pyramid

blocks = int(input("Enter the number of blocks: ")) # Takes the input from user as integer for number of blocks

height = 0 #  As the height is only measured if fully completed, the counter starts at 0

layer = 1 # It defines the layer of pyramid

# Using while loop to calculate the number of blocks left after each iteration and continue until layer is equal to or less than blocks
while layer <= blocks:
    blocks = blocks - layer
    layer+=1
    height +=1

# Output the height of the pyramid    
print("The height of the pyramid:", height)


# Chapter 3.2.1.15 Collatz's hypothesis-20210922
# This lab is about creating a program which would test Collatz's hypothesis

c0 = int(input("Enter any non-negative and non-zero integer number: ")) # Prompt user to enter any non-negative and non-zero integer number
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
    print("steps =", step) # Prints the number of steps taken to achieve the goal

