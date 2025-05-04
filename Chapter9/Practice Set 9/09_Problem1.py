# Problem 1
# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

# f = open("./Practice Set 9/poems.txt")

# data = f.read()

# data1 = data.lower()
# f.close()

# if "twinkle" in data1:
#     print("The word 'twinkle' is present in the file.")
# else:
#     print("The word 'twinkle' is not present in the file.")

with open("./Practice Set 9/poems.txt") as f:
    data = f.read()
    if "twinkle" in data.lower():
        print("The word 'twinkle' is present in the file.")
    else:
        print("The word 'twinkle' is not present in the file.")
