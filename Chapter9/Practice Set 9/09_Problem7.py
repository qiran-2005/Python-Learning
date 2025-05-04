# Problem 7
# Write a program to find out the line number where python is present from ques 6.

with open("./Practice Set 9/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Yes, the word Python is present, Line no: {lineno}")
        break
    lineno = lineno+1

else:
    print("No, the word Python is not present.")
