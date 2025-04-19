# While Loops
# In while loops, the condition is checked first. If it evaluates to true, the body of the loop
# is executed otherwise not!
# If the loop is entered, the process of [condition check & execution] is continued until
# the condition becomes False.

# i = 1

# while (i < 6):
#     print(i)
#     i = i+1


# Quick Quiz 1
# Write a program to print 1 to 50 using a while loop.

# i = 1

# while (i <= 50):
#     print(i)
#     i += 1


# Quick Quiz 2
# Write a program to print the content of a list using while loops.
list = ["Qiran", 1, "Rehan", 20.0, True, 50]
a = len(list)

n = 0

while (n < a):
    print(list[n])
    n += 1
