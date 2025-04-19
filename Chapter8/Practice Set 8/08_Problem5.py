# Problem 5
# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

n = int(input("Enter a number: "))


# Function Definition
def starPattern(n):
    for i in range(n+1):
        print("*"*(n-i), end="")
        print(" " * (i-1), end="")
        print()


# Function call
starPattern(n)


# Recursive Method


# Function Definition
def pattern(n):
    if (n == 0):
        return
    print("*" * n)
    pattern(n-1)


pattern(3)
