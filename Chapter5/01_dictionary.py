# Dictionaries
# Dictionary is a collection of keys-value pairs.

marks = {
    "Qiran": 98,
    "Rehan": 70,
    "Imaan": 56
}
marks1 = {}  # Empty dictionary
# print(type(marks1))

print(marks, type(marks))

print(marks["Qiran"])

print(marks.items())

# Properties
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.


qiran = {
    "name": "Qiran",
    "age": 19
}

print(qiran)

qiran["age"] = 20

print(qiran["name"])
print(qiran)
