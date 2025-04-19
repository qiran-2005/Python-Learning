# Problem 8
# Write a python function to print multiplication table of a given number.

n = int(input("Enter a number: "))


# Function Definition
def mul(n):
    for i in range(1, 11):
        print(n*i)


mul(n)

# Problem 8
# Write a python function to print multiplication table of a given number.

# Function Definition


def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# Input with validation
try:
    n = int(input("Enter a number: "))
    print_multiplication_table(n)
except ValueError:
    print("Please enter a valid integer.")
