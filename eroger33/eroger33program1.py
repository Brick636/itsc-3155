# function returns first and last two characters of a user string
def letters():
    word = input("Please enter a string: ")
    print("The string is " + word)
# if the user string is less than a length of 2 print user error message
    if len(word) < 2:
        print("String is not long enough!")  
# else return the first and last two characters of the user string            
    else:
        newWord = word[0] + word[1] + word[len(word) - 2] + word[len(word) - 1]
        return(newWord)

print(letters())           