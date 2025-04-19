# Problem 2
# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter)

name = input("Enter your name: ")
date = input("Enter today's date: ")
print(letter.replace("<|Name|>", "Name").replace("<|Date|>", date))
