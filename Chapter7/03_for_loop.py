# For Loop
# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

for i in range(4):
    print(i)

list = [1, 5, "Qiran", True, 20.0]

for i in list:
    print(i)


string = "Qiran"

for i in string:
    print(i)


tuple = (1, 5, "Qiran", True, 20.0)

for i in tuple:
    print(i)

# For Loop with else
# An optional else can be used with a for loop if the code is to be executed when the
# loops exhausts.

for i in range(4):
    print(i)

else:
    print("For Loop is done iterating")


for i in range(5):
    if i == 3:
        print("Found 3, now breaking the for loop")
        break
    print(i)

else:
    print("Done")

# The else block after a for loop runs only if the loop completes without encountering a break.

# If the loop is interrupted with break, the else block is skipped.
