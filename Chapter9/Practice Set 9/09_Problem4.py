# Problem 4
# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.

word = "Donkey"
with open("./Practice Set 9/Problem4.txt") as f:
    data = f.read()
    if (word in data):
        dataNew = data.replace("Donkey", "######")

with open("./Practice Set 9/Problem4.txt", "w") as f:
    f.write(dataNew)
    print("File updated successfully.")
