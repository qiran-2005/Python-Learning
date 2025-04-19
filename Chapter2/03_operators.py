# Different types of Operators in Python

# 1. Arithematic Operators (+,-,*,/, and more)

a = 1
b = 9
# addition
c = a+b
print(c)
# subtraction
c = a-b
print(c)
# and you can perform any arithematic operations

# 2. Assignment Operators (=, +=, -=, and more)
d = 1  # = is used to assign a value to a variable

d += 4  # += operator is used to increment a variables value
print(d)  # d += 4, in this case a programmer is saying that increment the value previous of d by 4

d -= 10  # -= operator is used to decrement a variables value
print(d)  # d -= 4, in this case a programmer is saying that decrement the value previous of d by 10

# We can also use * and / inplace of + and - to perform assignment operations


# Comparision Operators (==, >, >=, <, != etc.)
# The return value of any comparision operator is always a boolean

# Logical operators (and, or, not)

# Truth Table of "AND"
print("\nTruth Table of AND")
print("True and True is", True and True)
print("True and False is", True and False)
print("False and True is", False and True)
print("False and False is", False and False)

# Truth Table of "OR"
print("\nTruth Table of OR")
print("True or True is", True or True)
print("True or False is", True or False)
print("False or True is", False or True)
print("False or False is", False or False)

# NOT Logical Operator
print(not (False))
print(not (True))
