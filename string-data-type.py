myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

"""
name = input("What is your name? ")
print(name)
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
"""


name = input("What is your name? ")
affilliation = input("Hello, Whcich political party are you an affilliate of?")
fbill = input("Do you support or reject the finance bill 2024?")
print("{}, You are a member of {} political party, and you {} the finance bill 2024".format(name,affilliation,fbill))
