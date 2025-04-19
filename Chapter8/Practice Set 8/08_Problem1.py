# Problem 1
# Write a program using functions to find greatest of three numbers.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))


# Function Definition
def greatestNumber(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        print(f"Number 1: {num1} is greatest")
    elif (num2 > num1 and num2 > num3):
        print(f"Number 2: {num2} is greatest")
    elif (num3 > num1 and num3 > num2):
        print(f"Number 3: {num3} is greatest")


# Function Call
greatestNumber(num1, num2, num3)
