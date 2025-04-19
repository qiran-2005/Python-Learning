# Problem 1
# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

if (a > b and a > c and a > d):
    print("a is greater")
elif (b > a and b > c and b > d):
    print("b is greater")
elif (c > b and c > a and c > d):
    print("c is greater")
elif (d > a and d > b and d > c):
    print("d is greater")
