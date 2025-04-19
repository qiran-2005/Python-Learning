# Problem 3
# Attempting problem 1 using while loop

# Write a program to print multiplication table of a given number using while loop.

num = int(input("Enter a number: "))

print("The multiplication table of ", num, "is: ")

i = 1

while (i <= 10):
    print(num*i)
    i += 1
