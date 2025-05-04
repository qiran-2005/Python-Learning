# The random-access memory is volatile, and all its contents are lost once a program
# terminates. In order to persist the data forever, we use files.

# In Python, we can use the built-in open() function to create a file object. The open() function takes two arguments: the name of the file and the mode in which to open it. The mode can be one of the following:
# 'r' - read (default mode)
# 'w' - write (overwrites the file if it exists, creates a new file if it does not exist)
# 'a' - append (adds to the end of the file if it exists, creates a new file if it does not exist)

f = open("file.txt")
data = f.read()
print(data)
f.close()
