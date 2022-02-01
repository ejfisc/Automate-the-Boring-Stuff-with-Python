# python comes with a set of modules called the standard library
# each module is a program that contains a related group of functions
# use the import keyword to import a module

import random
for i in range(5):
    print(random.randint(1, 10))


# you can import more than one module at a time, separating them by commas
import sys, os, math

# alternatively you could use from x import y, for example:
from random import *
# this would allow you to make calls to functions in random without the random. prefix
# however, using the full name makes for more readable code, so it is better to use the
# import random form of the statement

# you can use the sys.exit() function to terminate the program early

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')