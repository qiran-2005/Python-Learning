# Some of the commonly used functions to perform operations on or manipulate strings
# are as follows. Let us assume there is a string ‘str’ as follows:

name = "Qiran"

# Different string functions

print(len(name))
print(name.upper())
print(name.lower())
print(name.endswith("an"))
print(name.startswith("q"))
print(name.isdigit())
print(name.isalpha())
print(name.swapcase())


name1 = "qiran"
print(name1.capitalize())

name2 = "Qiran is a good good boy "
print(name2.title())
print(name2.split())
print(name2.find("good"))
print(name2.replace("good", "bad"))
print(name2.count("i"))

name3 = " Qiran"
print(name3.strip())
