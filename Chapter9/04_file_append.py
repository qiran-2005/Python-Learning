# Appending a file

string = "My name is Qiran"

f = open("file.txt", "a")

f.write(string + "\n")

f.close()
