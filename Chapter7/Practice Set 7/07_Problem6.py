# Problem 6
# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a number: "))

fact = 1
# i = 1


# if (num == 0 or num == 1):
#     print(f"Factorial of {num} is 1")


for i in range(1, num+1):
    fact = fact * i

print(f"Factorial of {num} is {fact}")
