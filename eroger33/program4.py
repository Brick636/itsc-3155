# function to take in an invoice of items and their values and sort the items by value
def invoice():

    numItems = 0
    invoiceItems = []

# while loop to add item name and item values as tuples to invoiceitems list    
    i = 1
    while i == 1:

        invoiceItems.append((input("input item name: "), input("input item value: ")))

# numItems increments each item added
        numItems += 1

# lets the user add another item or not
        choice = input("Add another item to the list?  (y/n) ")

        if choice == "y":
            i = 1
        elif choice == "n":
            i = 0    

# used bubblesort to sort the tuples based off their second value in ascending order
    for i in range(numItems - 1):
        for j in range(numItems - i - 1):
            if invoiceItems[j + 1][1] < invoiceItems[j][1]:
                tempList = []
                tempList = invoiceItems[j]
                invoiceItems[j] = invoiceItems[j+1]
                invoiceItems[j+1] = tempList

# loop through invoiceItems list and print the first elements first value, a space, and the second value    
    for i in range(numItems):
        print(invoiceItems[i][0] + " " +  invoiceItems[i][1])
        

invoice() 
