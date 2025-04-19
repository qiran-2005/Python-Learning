# Set Methods

empty_set = set()

empty_set.add(1)  # Adds an element in the an empty set or a well-defined set
empty_set.add(2)
empty_set.add(3)
print(empty_set)

print(len(empty_set))  # Prints the length of a set

empty_set.remove(3)  # Removes a specific element from a set
# empty_set.remove("Qiran")
print(empty_set)

# empty_set.clear()  # Clears the entire set and makes it an empty set
# print(empty_set)

set1 = empty_set.copy()  # Copies the entire set into a new one
print(set1)

# Union and Intersection are done in a seperate file
