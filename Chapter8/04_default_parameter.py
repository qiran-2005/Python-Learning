# We can have a value as default as default argument in a function.

# If we specify name = “stranger” in the line containing def, this value is used when no
# argument is passed.

# Function Definition
def goodDay(name, ending="Thank you"):
    print(f"Good Day {name}")
    print(ending)


# Function Call
goodDay("Qiran", "You are promoted")
