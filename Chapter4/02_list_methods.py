# List Methods

friends = ["Qiran", "and", "Akshath", "are",
           "Friends", "from", 5, "Years", True]

friends.append("Yes, it's True")
print(friends)  # adds an element at the end of the list

# this method inserts any value at any index of the list, 3 is the index and "is" is the value to be inserted
friends.insert(3, "is")
print(friends)

friends.pop(4)  # this method deletes an element at a sepcific index
print(friends)

friends.remove(5)  # This method removes a specific element from the list
print(friends)

friends.remove(True)  # This method removes a specific element from the list

friends.reverse()  # this method reverses all the indexes of the elements of the list
print(friends)


list1 = [1, 30, 8, 6, 100, 99, 20]
list1.sort()  # this method sorts a list
print(list1)
