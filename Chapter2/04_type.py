# TYPE() FUNCTION AND TYPECASTING.
# type() function is used to find the data type of a given variable in python.

print("String to Integer")
a = "10"  # Anything in between a double quote is a string in Python
print(type(a))

# To convert the variable a into an integer value we use int(a) and store it in a different variable for good understanding
b = int(a)
print(type(b))

print("\nFloat to Integer")
# Similarly we can change a float into an integer and an integer into a float or any valid conversions are allowed
c = 2.3
print(type(c))

d = int(c)
# When we convert a float into an integer, the value after the point gets completely ignored
print(type(d))
print(d)

print("\nInvalid Conversions")
# We cannot convert a string like "Qiran" into float or integer, it is invalid
e = "Qiran"
print("Type of e is", type(e))

f = int(e)
print("Type of f is", type(f))
# I will get an output like this: "f = int(e)
# ValueError: invalid literal for int() with base 10: 'Qiran'"
