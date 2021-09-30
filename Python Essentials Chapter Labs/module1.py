#15) create a function called caseChanger which takes a string argument written all in lower case
#It will output all letters in lowercase except e which it will convert to capital E (10 marks)
#Perform a test print which using hello: caseChanger("hello") this should
#print hEllo to the console.

# Creates a caseChanger function
def caseChanger(user_word):
    new_word = ""
    for letter in user_word:
        if letter != "e":
            new_word+=letter
        else:
            new_word+="E"
    return(new_word)
    
print(caseChanger("hello"))
##################################################### 