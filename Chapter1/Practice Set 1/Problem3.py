# Problem 4: Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. (Done using AI)

import os

# Specify the directory path
# Replace '/path/to/directory' with the actual path of the directory you want to list
directory_path = '/path/to/directory'

try:
    # List all entries in the directory
    # os.listdir() returns a list of file and directory names in the specified directory
    entries = os.listdir(directory_path)

    # Print a message indicating the directory contents
    print(f"Contents of '{directory_path}':")

    # Loop through each entry in the directory and print it
    for entry in entries:
        print(entry)

except FileNotFoundError:
    # Handle the case where the directory doesn't exist
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    # Handle the case where the program doesn't have permission to access the directory
    print(f"Permission denied to access '{directory_path}'.")


# Problem 5: Label the program written in problem 4 with comments. (Done using AI)
