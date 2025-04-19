# String is a data type in python.

# String is a sequence of characters enclosed in quotes.

# We can primarily write a string in these three ways.

# Strings are immutable.

a = "Qiran"  # this is a string
b = 'Qiran'  # this is also a string
c = '''Qiran'''  # this is also a string

print(type(a), type(b), type(c))

print(len(a), len(b), len(c))

# String Slicing
name = a[0:3]
print(name)

character1 = a[1]
print(character1)

# Negative Slicing

# If i don't write any value after :, then it is considered length-1
negative_name = a[-3:]
print(negative_name)

negative_character1 = a[-4]
print(negative_character1)

# STRING SLICING WITH SKIP VALUE

d = a[0:6:2]
print(d)
