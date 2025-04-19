# Break, Continue and Pass statements

# Break Statement
# ‘break’ is used to come out of the loop when encountered. It instructs the program to –
# exit the loop now.

for i in range(10):
    if (i == 8):
        break
    print(i)


# Continue Statement
# ‘continue’ is used to stop the current iteration of the loop and continue with the next
# one. It instructs the Program to “skip this iteration”.

for i in range(10):
    if (i == 8):
        continue
    print(i)

# Pass Statement
# pass is a null statement in python.
# It instructs to “do nothing”.

for i in range(10):
    if (i == 8):
        pass
