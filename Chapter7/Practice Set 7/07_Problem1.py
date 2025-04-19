# Problem 1
# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter a number: "))

print("The multiplication table of ", num, "is: ")


for i in range(1, 11):
    print(num*i)
