# Write a program to print multiplication table of n using for loops in reversed order.

num = int(input("Enter a number: "))

for i in reversed(range(1, 11)):
    print(num*i, end="")
    print()
