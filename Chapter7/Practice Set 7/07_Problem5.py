# Problem 5
# Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Enter a number: "))

sum = 0
i = 1

while (i <= num):
    sum = sum+i
    i += 1

print(sum)
