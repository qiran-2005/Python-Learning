# Problem 7
# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter the post: ")

# Convert both the post and the search term to lowercase to make the search case-insensitive
if ('harry' in post.lower()):
    print("The post talks about Harry.")
else:
    print("The post does not talk about Harry.")
