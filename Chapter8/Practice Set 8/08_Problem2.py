# Problem 2
# Write a python program using function to convert Celsius to Fahrenheit.

# Function Definition
def tempConverter(C):
    F = (C * (9/5)) + 32
    return F


C = int(input("Enter the temprature in Celsius: "))

temp_Fahrenheit = tempConverter(C)
print(f"The temprature in Fahrenheit is: {round(temp_Fahrenheit, 2)}°F")
