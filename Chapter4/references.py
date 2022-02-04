# this is an example that explains how variables act as references to data in memory
spam = 42
cheese = spam
spam = 100
print(spam) # 100
print(cheese) # 42
# when you assign spam to cheese, you are actually copying the reference to cheese, so both spam
# and cheese refer to the 42 value in memory. WHen you change spam to 100, you are creating a new 100
# value and storing a reference to it in spam. This doesn't affect the value in cheese, which is a 
# reference to the 42
spam = [0, 1, 2, 3, 4, 5]
cheese = spam # the reference is being copied, not the list
cheese[1] = 'hello' # this modifies the list value
print(spam)
print(cheese)
# they are the same because both spam and cheese refer to the same list
# there is only one list, you didn't create a new list for cheese nor did you 
# create a new list by modifying cheese[1]

# id() function:
# all values in python have a unique identity that can be obtained using id()
print(id('howdy'))
# when python runs the previous instruction, it creates the 'howdy' string in the computer's memory
# the address where the value is stored is returned by id(), and different each time the code is run.
# because it is a string, 'howdy' cannot be changed. if you "change" the string in a variable, a new string
# object is being made at a different place in memory and the variable refers to this new string
var = 'test'
print(id(var))
var += 'ing'
print(id(var)) # var now refers to a completely different string
