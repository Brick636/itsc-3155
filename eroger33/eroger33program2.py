# function takes the range two user inputs and prints out numbers divisible by 7 but not 5
def numRange():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a larger number than previously entered: "))

# loop through the range of the two numbers
    for numbers in range(num1, num2):

# if the current number modulo 7 is equal to zero and modulo 5 is not equal to 0 print the number        
        if numbers % 7 == 0 and numbers % 5 != 0:
            print(numbers)

numRange()