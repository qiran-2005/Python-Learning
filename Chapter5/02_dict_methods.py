# Dictionaries Methods

marks = {
    "Qiran": 98,
    "Rehan": 70,
    "Imaan": 56
    # key: value
}

# print(marks.items())  #prints all the key and value pairs in such a way that kaeys and values are in different tuples which are inside a list. e.g. dict_items([('Qiran', 98), ('Rehan', 70), ('Imaan', 56)])

# print(marks.keys())  #prints all the keys inside a dictionary

# print(marks.values())  #prints all the values assigned to the keys inside a dictionary

# marks.update({"Qiran": 100}) #updates the value of a key is previously available, and adds the key and value if not previously available

# print(marks)

# print(marks.get("Rehan1"))  # Prints None if the key does not exists
# print(marks["Rehan1"])  # Returns an error if the key does not exists

# marks.clear()  #clears the entire dictionary

# marks1 = marks.copy()  #copies the entire dictionary, in this case "marks", into a new dictionary

# student1 = marks.pop("Imaan")  # Deletes a specific key along with it's value
# print(student1)
# print(marks)

del marks["Qiran"]  # Deletes a key-value pair from the dictionary.
print(marks)
