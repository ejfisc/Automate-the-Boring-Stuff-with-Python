# lists aren't the only data type that represent ordered sequences of values
# sequence data types: lists, strings, range objects (from range()) and tuples
# string example:
import this


name = 'Ethan'
print(name[0]) # this is 'E'
print(name[-2]) # this is 'a'
print(name[1:4]) # this is 'tha'
print('x' in name) # False
print('d' not in name) # True
print('Et' in name) # True

for i in name:
    print(i)

# the difference between a list and a string is that lists are mutable, they can be modified
# if you try to do something like name[2] = 'j' That will result in an error, because you cannot
# change a string

# you can create a new string using slices from the previous one
firstAndLastName = 'Ethan Fischer'
fullName = firstAndLastName[:5] + ' Jonah ' + firstAndLastName[6:]
print(fullName)

# the second line of code here isn't modifying the list abc, it is overwriting the old list value
abc = ['a', 'b', 'c']
abc = ['d', 'e', 'f']
print(abc) # prints ['d', 'e', 'f']

# tuples are almost identical to lists BUT they're defined using () instead of [] and 
# like strings, tuples are immutable. YOu cannot modify, append or remove items in a tuple
# attempting to do so will result in an error
thisIsATuple = (1, 2, 3, 4, 5)
print(thisIsATuple[0]) # prints 1
print(thisIsATuple[1:4]) # prints [2, 3, 4]

# if you have only one value in your tuple, indicate this by placing a trailing comma inside the
# parentheses, otherwise Python will think you've just typed a value inside regular parentheses
print(type(('hello',)))
print(type(('hello')))

# use tuples to convey that you don't intend for that sequence of values to change. 
# Because tuples are immutable, python can implement some optimizations that make code using tuples
# slightly faster than code using lists

# convert between tuples and lists
print(list((1, 2, 3)))
print(tuple([1, 2, 3]))
print(list('hello'))

