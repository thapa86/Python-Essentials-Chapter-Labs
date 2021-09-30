##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: Anil Thapa
##Course Number: SIMR 20-001
##Student Number: 21171686

##complete each task which is shown as a comment. 
#complete each task directly below the comment
#each task shows a task number, and number of marks awarded
#on each task requiring an output, ensure the task goes on a separate line (unless stated)
#and ensure that it states the task number prior to any output e.g. Task 11 
#upload your final file to your assigned folder share on class.net
# \\192.168.68.114\test-sub\regiNumber

#####################################################
#Section 1 25 Marks


#1) Create and Assign a type float variable called fltOne the value 10 (3)
fltOne = float(10)

#2) Create and Assign a type float variable called fltTwo the value 20 (3)
fltTwo = float(20)

#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)
fltThree = float(fltTwo * fltOne)

#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)
stringOne = "The product of fltOne and fltTwo = "

#5) On the console, output stringOne and fltThree (in that order) (3)
print("Task 5") # This will print 'Task 5'
print(stringOne, fltThree)

#6) increment fltOne  (3)
fltOne = fltOne+1 # This will increment the value of fltOne by 1

#7)  prompt the user to provide an input to fltTwo with the message "Please provide another number for fltTwo". Ensure a float is given (4)
fltTwo = float(input("\nPlease provide another number for fltTwo")) #'\n' will start this output in new line

#8) on the console, output the product of fltOne and flotTwo with a suitable message (3) 
print("\nTask 8") # This will print 'Task 8'
print("The product of fltOne and fltTwo is: ", fltOne * fltTwo)

#####################################################
#Section 2 35 Marks

#8) take the input from fltTwo and apply a decision based on the number inputted . 
#The decision should be based on if the user inputs a number below 100
if fltTwo < 100:
#the code should output "below 100" (5)
    print("\nTask 8") # This will print 'Task 8'
    print("below 100") # This will print 'below 100'

#9) take the difference between of fltOne and fltTwo (fltOne - fltTwo)
difference = fltOne-fltTwo # This will subtract fltTwo from fltOne

#Using if, else and elif, output the following: 
#If the difference is below 0, output "below 0"
if fltOne * fltTwo < 0:
    print("\nTask 9") # This will print 'Task 9'
    print("below 0") # This will print 'below 0'

#if the product is 0 output "value is zero"
elif fltOne * fltTwo > 0:
    print("above 0") # This will print 'above 0'
#if the product is above 0 output "above 0" (8)
elif fltOne * fltTwo == 0:
    print("value is zero") # This will print 'value is zero'


#10) create a list called listOfInts (4)
listOfInts = []

#11 part a) create a for loop to iterate through the above list and populate the list with 
#{4,6,8,10,12,14,16,18,20,22}. Output the list to the console with a suitable message(7)

for i in range(4,23): # for loop which will iterate for i value from 4 to 23
    if i % 2 == 0: # if the modulo of the value is equal to 0, then it is an even number
        listOfInts.append(i) # if even number, list will be appended with new even number

# The following will output 'Task 11 part a) in new line with new listOfInts
print("\nTask11 part a)")
print(listOfInts)

#11 part b) create a for loop to iterate through the above list and 
#multiply each value by three assigning the new value to the respective 
#index in the list. The list should now look like {12,18,24.....} (8)

for i in range(len(listOfInts)): # For loop which will iterate over the lenght of the list which is 10, i.e 0 to 9
    listOfInts[i] = listOfInts[i] * 3 # This will multiply each element in the list by 3

#11 part c )output listOfInts to the screen with a suitable message (3)
print("\nTask 11 b)")
print("The listOfInts multiplied by 3 is:", listOfInts)

#####################################################
#Section 3 20 marks

#14) create a function which calculates a decrease of a given percentage (10 marks)
# the function should be called calcPerc
#the function should take a cost parameter and a percentage parameter
#it should return the cost less the percentage amount
#For example if the paramenters are cost = 100 and percentage = 50, it should return 50. 
#For another example, if the parameters are cost = 50 and percentage = 10, it should return 45.
#The percentage value should assume 10% if no value is given

def calcPerc(cost,percentage=10): # this creates a function with two parameters, cost and percentage. Percentage with default argument of '10'
    return (cost - (percentage/100) * cost) # any percentage of some value is given by multiplying the some value and dividing by 100

print("\nTask 14")
#print a test to the screen with cost set as 50 and percentage set as 10
print(calcPerc(50,10))

#15) create a function called caseChanger which takes a string argument written all in lower case
#It will output all letters in lowercase except e which it will convert to capital E (10 marks)
#Perform a test print which using hello: caseChanger("hello") this should
#print hEllo to the console.

# Creates a caseChanger function which will take user_word and checks if it has lowercase 'e'
# If it has lowercase 'e', it will change it to uppercase 'E'
def caseChanger(user_word):
    new_word = "" # Defining a new_word variable which will store new_word with e changed to upper case
    
    # For loop to check if the word has e or not
    for letter in user_word:
        if letter != "e":
            new_word+=letter # if the letter is not 'e', it will be added to the new_word
        else:
            new_word+="E" # If the letter is 'e', it will be changed to 'E' and added to the new_word
    return(new_word) # Returns the new_word
print("\nTask 15")    
print(caseChanger("hello\n"))

##################################################### 
#Section 4 20 marks

#16)a) Create a list that represents a set of students. The list should contain the following
#students: Clark,Horan,Rai,White,Cooper,Jones,Cox,Smith (4 marks)
list_of_students = ["Chris", "Horan", "Rai", "White", "Cooper","Jones","Cox","Smith"]

#b) use a method to order the students so that they are in alphabetical order (3 marks)
list_of_students.sort() # 'sort()' method will sort the list of students in alphabetical order

print("Task 16")
print(list_of_students) # Print the list of students sorted in an alphabetical order

#17) create a tuple that represents exam marks with the following data. (4 marks)
#These are the respective exam marks for the alphabetically ordered student list
# 65,66,67,80,90,65,65,93

exam_marks = (65,66,67,80,90,65,65,93) # This will create a tuple named 'exam_marks'
print(exam_marks) # This will print all elements of tuple 'exam_marks'

#18) Dictionary question (9 marks)
#create a dictionary
student_marks = {} # This creates an empty dictionary called 'student_marks'

#write code which adds both the student and a their corresponding mark. 
for i in range(len(list_of_students)): # for loop to iterate through the range equal to lenght of the list_of_students list

    # This will pair up each key with corresponding value and add it to the dictionary.
    # Elements in list_of_students used as keys and elements in tuple 'exam_marks' used as values
    student_marks[list_of_students[i]] = exam_marks[i] 

print("\nTask 18") # Prints 'Task 18' in new line
print(student_marks) # Print the student marks dictionary

#do not perform this long hand (as in writing out the values above). Use data
#from the existing tuples above to create the dictionary
