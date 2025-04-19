# Recursive Function
# Example: Factorial
'''
Factorial(0) = 1
Factorial(1) = 1
Factorial(2) = 2 x 1
Factorial(3) = 3 x 2 x 1
Factorial(4) = 4 x 3 x 2 x 1
Factorial(5) = 5 x 4 x 3 x 2 x 1
Factorial(n) = n * n-1 * ..... 3 x 2 x 1

factorial(n) = n * factorial(n-1)
'''

# Function Definition


def factorial(n):
    if (n == 1 or n == 0):
        return 1
    return n * factorial(n-1)


n = int(input("Enter a number: "))

print(f"Factorial of {n} is: {factorial(n)}")
