#Imagine a list - not very long, not very complicated, just a simple list containing some integer numbers. 
#Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.
#simple_list = [1,2,3,3,4,6,7,7,7,8,9]
simple_list = int((input("Please enter your number here")))
unique_list = []

for i in range(len(simple_list)):
    if simple_list[i] not in unique_list:
        unique_list.append(simple_list[i])

print(unique_list)

#Your task is to write a program which removes all the number repetitions from the list. 
#The goal is to have a list in which all the numbers appear not more than once.

#Note: assume that the source list is hard-coded inside the code - you don't have to enter it from the keyboard. 
#Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.

#Hint: we encourage you to create a new list as a temporary work area - you don't need to update the list in situ.


#print("The list with unique elements only:")
#print(my_list)


