# Problem 5
# Write a program which finds out whether a given name is present in a list or not

name_list = ["Qiran", "Rehan", "Imaan", "Hamdan"]
name = input("Enter your name: ")

if (name in name_list):
    print("Name is already in the list")

elif (name not in name_list):
    name_list.append(name)
    print("Name is added to the list")
