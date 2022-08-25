def letters():
    word = input("Please enter a string: ")
    print("The string is " + word)


    if len(word) < 2:
        print("String is not long enough!")
    else:
        newWord = word[0] + word[1] + word[len(word) - 2] + word[len(word) - 1]
        print(newWord)

letters()           