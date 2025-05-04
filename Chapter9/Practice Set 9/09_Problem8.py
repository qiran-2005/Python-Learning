# Problem 8
# Write a program to make a copy of a text file “this. txt”

with open("./Practice Set 9/python.txt") as f:
    content = f.read()

with open("Practice Set 9/python1.txt", 'w') as f:
    f.write(content)

print("File updated successfully.")
