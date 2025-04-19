# SETS
# a set is an unordered collection of unique elements, defined by curly braces {} or the set() constructor.

set1 = {1, 4, 3, 3, 3, 8, 9, "Qiran"}
print(set1)

empty_set = set()  # This is how an empty set is declared

print(type(set1))
print(type(empty_set))

# properties
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

# empty_set.add(1)  # Adds an element in the an empty set or a well-defined set
# empty_set.add(2)
# print(empty_set)

# print(len(empty_set))  # Prints the length of a set

set1.remove(3)  # Removes a specific element from a set
set1.remove("Qiran")
print(set1)
