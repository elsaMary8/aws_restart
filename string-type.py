"""
myString = "\"Hey this is Elsa!\""
print(myString)
print(type(myString))
print(str(myString) + " is of type" + str(type(myString)))


firstString = "New"
secondString = "York"
thirdString = firstString + secondString
print(thirdString)

"""

name = input("What is your name? ")
"""print(name)"""

color=input("What is your favourite color? ")
animal=input("What is your favourite animal? ")

print("{}, you like a {}  {}!" .format(name,color,animal))