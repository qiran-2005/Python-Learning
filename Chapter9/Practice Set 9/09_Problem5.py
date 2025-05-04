# Problem 5
# Repeat program 4 for a list of such words to be censored.

words = ['bad', 'ugly', 'stupid']

with open("./Practice Set 9/Problem5.txt") as file:
    text = file.read()
    for word in words:
        text = text.replace(word, '#' * len(word))

with open("./Practice Set 9/Problem5.txt", 'w') as file:
    file.write(text)

print("Censored text written to file.")
