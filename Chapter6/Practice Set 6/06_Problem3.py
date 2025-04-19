# Problem 3
# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams


comment = input("Enter your comment: ")

# if (comment == "Make a lot of money" or comment == "buy now" or comment == "subscribe this" or comment == "click this"):
#     print("This is a Spam Comment")

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

if ((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")
