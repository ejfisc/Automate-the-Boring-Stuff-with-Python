# dictionaries are mutable like lists, but instead of using indexes, dictionaries use keys which can
# be many different data types. A key with is associated value is called a key-value pair.
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# this assigns a dictionary to the myCat variable. The dictionary's keys are size, color, and disposition
print(myCat['size']) # 'fat'
print('My cat has ' + myCat['color'] + ' fur.')

# a key can still be an integer but they do not have to start at 0 and can be any nummber
spam = {12345: 'Luggage combination', 42: 'The Answer'}

# unlike lists, items in dictionaries are unordered
# 2 dictionaries are considered identical if they contain the same key-value pairs, order 
# does not matter
labc = ['a', 'b', 'c']
lcba = ['c', 'b', 'a']
print(labc == lcba) # False
d123 = {1: 'a', 2: 'b', 3: 'c'}
d321 = {3: 'c', 2: 'b', 1: 'a'}
print(d123 == d321) # True

# because dictionaries are not ordered, they can't be sliced like lists
# trying to access a key that does not exist in a dictionary will result in a KeyError

# use the keys() method to get the keys of a dictionary
for k in myCat.keys():
    print(k)

# use the values() method to get the values of a dictionary
for v in myCat.values():
    print(v)

# use the items() method to get the key-value pairs of a dictionary
for i in myCat.items():
    print(i) # notice that the items value returned by the items() method are tuples of the key and value

# you can also use the multiple assignment trick to assign the key and value to separate variables
for k, v in myCat.items():
    print('Key: ' + k + ' Value: ' + v)

# the in and not in operators work on dictionaries as well to check if a key or value
# is or isn't in the dictionary

# dictionaries have a get() method to retrieve a value, you can pass a fallback value as a 
# second argument if that key does not exist in the dictionary
picnicItems = {'apples': 5, 'cups': 2, 'basket': 1, 'sandwiches': 2, 'blanket': 1}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# the setdefault() method sets a value in a dictionary for a key only if that key does not already have a value
spam = {'name': 'Pooka', 'age': 5}
print(spam.setdefault('color', 'black'))
print(spam)
# if the key already exists, the setdefault() method returns the key's value
print(spam.setdefault('color', 'white'))
