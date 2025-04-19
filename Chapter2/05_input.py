# Input Function
# This function allows the user to take input from the keyboard as a string (by default/if not specified).

a = input("Enter a number: ")

b = input("Enter another number: ")

print("User inputs are: ", a, "and", b)

print(type(a), type(b))
# In this state if you enter a number it will be stored in the variable as a string

# To over come this we have to define the type of input we require the end user to give.
# So here's how
c = int(input("Enter a number: "))

d = int(input("Enter another number: "))

print("User inputs are: ", c, "and", d)
print(type(c), type(d))
