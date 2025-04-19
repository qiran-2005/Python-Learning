# Problem 6
# Write a python function which converts inches to cms.

inche = float(input("Enter length in inches: "))


# Function Definition
def inche_to_cm(inche):
    cm = inche * 2.54
    return cm


a = inche_to_cm(inche)

print(f"Measurement in cm is: {a}")
