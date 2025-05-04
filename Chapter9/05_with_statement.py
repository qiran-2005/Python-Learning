# With Statement

# The with statement is used to wrap the execution of a block with methods defined by a context manager.
# It is commonly used for resource management and exception handling.

string = "My age is 19"

with open("file1.txt", "w") as f:
    f.write(string + "\n")
