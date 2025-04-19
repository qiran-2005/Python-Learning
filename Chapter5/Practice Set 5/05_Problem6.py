# Problem 6
# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

name_lang = {}

key1 = input("Enter your name: ")
value1 = input("Enter your fav language: ")
name_lang.update({key1: value1})

key2 = input("Enter your name: ")
value2 = input("Enter your fav language: ")
name_lang.update({key2: value2})

key3 = input("Enter your name: ")
value3 = input("Enter your fav language: ")
name_lang.update({key3: value3})

key4 = input("Enter your name: ")
value4 = input("Enter your fav language: ")
name_lang.update({key4: value4})

print(name_lang)
