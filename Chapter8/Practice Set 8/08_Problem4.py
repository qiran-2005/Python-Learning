# Problem 4
# Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter a number: "))


# Function Definition
def adding_Nat_nums(n):
    if (n == 0):
        return 0
    return n + adding_Nat_nums(n-1)


a = adding_Nat_nums(n)

print(f"Sum of the natural numbers is {a}")
