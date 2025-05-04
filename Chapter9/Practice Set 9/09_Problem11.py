# Problem 11
# Write a python program to rename a file to “renamed_by_ python.txt.

with open("./Practice Set 9/python.txt") as f:
    content = f.read()

with open("./Practice Set 9/new_python.txt", 'w') as f:
    f.write(content)
