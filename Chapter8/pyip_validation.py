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

# you can pass a string to a pyip function to display a prompt:
age = pyip.inputInt('Enter your age: ')
print(age)

# pass an array to inputChoice() and inputMenu() to restrict the user's response
fruitChoice = pyip.inputChoice(['apple', 'banana', 'orange', 'watermelon'], prompt='Choose your favorite fruit: ')
print(fruitChoice)

fruitMenu = pyip.inputMenu(['apple', 'banana', 'orange', 'watermelon'], prompt='Choose your favorite fruit: \n')
print(f"You chose {fruitMenu}!")

# the inputNum(), inputInt() and inputFloat() functions also have min, max, greaterThan, and lessThan keyword arguments
response = pyip.inputNum('Enter num at least 4: ', min=4) # x >= 4
response = pyip.inputNum('Enter num greater than 4: ', greaterThan=4) # x > 4
response = pyip.inputNum('Enter num at least 4 and less than 6: ', min=4, lessThan=6) # 4 <= x < 6

# by default, blank input isn't allowed unless the blank keyword argument is set to True
response = pyip.inputNum('Enter blank: ', blank=True)
print(response) # ''

# you can use the limit, timeout keyword arguments to stop asking the user for input after a certain number of 
# tries or amount of time (will throw a RetryLimitException or TimeOutException respectively)
response = pyip.inputNum('Enter a num in 2 attempts: ', limit=2)
response = pyip.inputNum('Enter a num in 10 seconds: ', timeout=10)

# when you use these keyword arguments and also pass a default keyword argument, the function returns the default
# value instead of raising an exception
response = pyip.inputNum('Enter a num in 2 attempts: ', limit=2, default='N/A')
print(response)

# use the allowRegexes and blockRegexes keyword arguments to specify whether an input is allowed or not
# for example, you could allow Roman Numerals in the inputNum() function
response = pyip.inputNum('Enter a roman numeral: ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# note that this only affects what letters the inputNum() will accept from the user, the user can still
# enter invalid roman numerals such as 'XVX' or 'MILLI' because the regex accepts those strings
response = pyip.inputNum('Enter an odd number: ', blockRegexes=[r'[02468]$'])

# if you specify both allow and block regexes, the allow list will override the block list
response = pyip.inputStr('Enter a word that starts with "cat": ', allowRegexes=[r'caterpillar', r'category'], blockRegexes=[r'cat'])

# the pyip functions save you from writing tedious input validation code yourself, but if you want to perform your
# own custom validation logic, you can write a function and pass it to inputCustom()
# i.e. say you want the user to input a series of digits that adds up to 10
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers) # return an int form of numbers

response = pyip.inputCustom(addsUpToTen, prompt='Enter numbers that add up to 10: ') # no parentheses after the function