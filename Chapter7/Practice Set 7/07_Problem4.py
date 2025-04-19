# Problem 4
# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number: "))

if (num <= 1):
    print("Invalid number")

for i in range(2, num):
    if (num <= 1):
        print("Invalid number")
        break

    elif (num % i) == 0:
        print(f"Number: {num} is not prime")
        break

else:
    print(f"Number: {num} is prime")
