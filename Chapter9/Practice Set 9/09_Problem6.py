# Problem 6
# Write a program to mine a log file and find out whether it contains ‘python’.

with open("./Practice Set 9/log.txt") as f:
    content = f.read()

if ("Python" in content):
    print("Yes, the word Python is present.")

else:
    print("No, the word Python is not present.")
