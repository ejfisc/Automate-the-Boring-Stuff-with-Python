#! python3
# pyip_validation.py - showcase of the PyInputPlus module and its methods

import pyinputplus as pyip

"""
inputStr() - like the built in input() function but has the general pyinputplus features
inputNum() - ensures the user enters a number and returns an int or float
inputChoice([]) - ensures the user enters one of the provided choices 
inputMenu([]) - similar to inputChoice() but provides a menu with numbered or lettered options
inputDatetime() - ensures the user enters a date and time
inputYesNo() - ensures the user enters a 'yes' or 'no' response
inputBool() - ensures the user enters a 'True' or 'False' response
inputEmail() - ensures the user enters a valid email address
inputFilePath() - ensures the user enters a valid file path and filename
inputPassword() - like the built in input() funciton but displays * characters as the user types so that passwords are hidden
These functions will automatically reprompt the user for as long as they enter invalid input
"""

# just as you can pass a string to input() to provide a prompt:
age = input('Enter your age: ')
print(age)

# you can pass a string to a pyip function's prompt keyword argument to display a prompt:
age = pyip.inputInt(prompt='Enter your age: ')
print(age)

# pass an array to inputChoice() and inputMenu() to restrict the user's response
fruitChoice = pyip.inputChoice(['apple', 'banana', 'orange', 'watermelon'], prompt='Choose your favorite fruit: ')
print(fruitChoice)

fruitMenu = pyip.inputMenu(['apple', 'banana', 'orange', 'watermelon'], prompt='Choose your favorite fruit: \n')
print(f"You chose {fruitMenu}!")

