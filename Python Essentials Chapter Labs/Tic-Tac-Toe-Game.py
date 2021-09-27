#TIC-TAC-TOE GAME
#Date created: 20210926
#Created by: Anil Thapa

#importing random module 
import random

#Code to create board using lists within lists and populate each of the 9 spaces on 
#the board with a "_"
tttBoard = [["-" for i in range(3)] for j in range(3)]

# Defining win_conditions for the game
win_1 = tttBoard[0][0]==tttBoard[0][1]==tttBoard[0][2]
win_2 = tttBoard[1][0]==tttBoard[1][1]==tttBoard[1][2]
win_3 = tttBoard[2][0]==tttBoard[2][1]==tttBoard[2][2]
win_4 = tttBoard[0][0]==tttBoard[1][0]==tttBoard[2][0]
win_5 = tttBoard[0][1]==tttBoard[1][1]==tttBoard[2][1]
win_6 = tttBoard[0][2]==tttBoard[2][2]==tttBoard[2][2]
win_7 = tttBoard[0][0]==tttBoard[1][1]==tttBoard[2][2]
win_8 = tttBoard[2][0]==tttBoard[2][1]==tttBoard[0][2]
win=False

# Defining the list of row index and column index so that random module can be called to generate random number from the list
row_index = [0,1,2]
column_index =[0,1,2]

#Minimum exercise
# Assuming the number of turns to be 30
for turns in range(10):

    for elements in tttBoard:
        print("\nCurrent Board:")
        if elements != "x" or "o":
            
            # print the board to the output
            for elements in tttBoard:
                print(elements)

            user_row = random.choice(row_index) # using random.choice to select random number for row index
            user_column = random.choice(column_index) # using random.choice to select random number for column index
            confirm = input("\nDo you want to proceed? Press Enter") # Pressing return key will continue adding "o" to the array
            tttBoard[user_row][user_column]="o" # Adding the "o" to the array

        if "-" not in elements: # Display if pre-defined value is replaced by "o"
            print("Gameover\n")

print("The next one is extension exercise")

#Extension Exercise  
#Game loop using 30 as maximum number of turns
for turns in range(20):
    print("\nCurrent Board:")

    #At the start of each iteration, the board will be printed to the screen
    for elements in tttBoard: # Will publish 3 x 3 lists
        print(elements)
    #if statement to check if the space in the list already contains "x" or "o"
    if tttBoard[0][0]!=tttBoard[0][1]!= tttBoard[0][2]!="x" or "o":       
        user_row = int(input("Enter a row: ")) # row index as input from user 
        user_column = int(input("Enter a column: ")) # column index as input from user
        game = input("Enter o or x (q to quit): ") # Prompt user to enter values
        
        # if entered value above is 'q', the game ends
        if game =="q":
            quit()
        # if statement to check if the list index values(entered row, column) contains prepopulated string "-" or not
        if tttBoard[user_row][user_column] == "-":
            tttBoard[user_row][user_column]=game # if space contains "-" value, "x" or "o" will be entered to the array
        
        # Else statement to prompt user to enter different values if space already populated with "x" or "o"    
        else:
            user_row = int(input("\nEnter a different row: "))
            user_column = int(input("Enter a different column: "))
            game = input("Enter o or x (q to quit): ")
            if game =="q":
                quit()
            tttBoard[user_row][user_column]=game
    
    # if single top line of the array has equal values, the game will end       
    if (tttBoard[0][0]==tttBoard[0][1]== tttBoard[0][2]):
        print("Congratulations!!! You won")
    
        




 

