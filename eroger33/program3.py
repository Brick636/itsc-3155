# function to combine two dictionaries, and add the sum of duplicate key values
def dictionary():

# placeholders for the final dictionary and dictionary key values for the for loop
    finalDict = {}
    dictKeyValues = 0

# user input for the amount of entries of dictionary 1 and 2
    numEntries = int(input("How many enrties to dictionary 1 will you enter? "))
    dict1 = {}

    numEntries2 = int(input("How many entries to dictionary 2 will you enter? "))
    dict2 = {}

# user input for the key values and data values for dictionary 1 and 2
    for i in range(numEntries):
        dict1[input("Add a letter for the key value of dictionary 1: ")] = input("Add a number for the data of dictionary 1: ")

    for i in range(numEntries2):
        dict2[input("Add a letter for the key value of dictionary 2: ")] = input("Add a number for the data of dictionary 2: ")

# combine the two dictionaries together
    finalDict = dict1 | dict2

# nested for loop to add data values of the matching key values together
    for i in dict1:
        dictValue1 = dict1.get(i)
        for j in dict2:
            dictValue2 = dict2.get(j)
            if i == j:   
                dictKeyValues = int(dictValue1) + int(dictValue2)
# after a match is found change the data value of key value "i" in finalDict to dictKeyValue
                finalDict[i] = dictKeyValues    

# displays dictionary 1, 2 and final dictionary
    print(dict1)
    print(dict2)
    print(finalDict)

dictionary()