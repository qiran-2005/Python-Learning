# Problem 4
# Write a program to find whether a given username contains less than 10
# characters or not.

name = input("Enter your fullname: ")

a = len(name)

if (a < 10 and a > 0):
    print("Your name has less than 10 characters.", a)

elif (a <= 0):
    print("Invalid name.")

else:
    print("Your name has more than 10 characters.", a)
