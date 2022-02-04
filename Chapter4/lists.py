# this is a list:
# [1, 2, 3]
# this list value refers to the list itself
li = ['dog', 'cat', 'fish', 'snake']
# li variable is still assigned only one value:  the list value, but the list 
# value itself contains other values

# this is an empty list
emptyList = []

# list indeces start at 0
print(li[0]) # this is 'dog'
print(li[1]) # this is 'cat'
print(li[2]) # this is 'fish'

# 2d list:
li2 = [['a', 'b', 'c'], [1, 2, 3]]
print(li2[0][0]) # this is 'a'
print(li2[0][2]) # this is 'c'
print(li2[1][0]) # this is 1
print(li2[1][2]) # this is 3

# negative indexes:
# the integer -1 refers to the last index in a list, 
# -2 refers to the second-to-last index and so on
print(li[-1]) # this is 'fish'
print(li[-2]) # this is 'cat'

# slices are used to get multiple values from a list
print(li[0:3]) # this is '['dog', 'cat', 'fish']' also same as li[0:-1]
print(li[1:3]) # this is '['cat', 'fish']'
# leaving out the first index is the same as using 0
# leaving out the second index is the same as using the length of the list
# using [:] will return the whole list

# get the length of a list with len()
print(len(li)) # this is 4

# list assignment works the same as any other language
print(li[1])
li[1] = 'feline'
print(li[1])

# lists can be concatenated and replicated just like strings
numList = [1, 2, 3]
abcList = ['a', 'b', 'c']
concatList = numList + abcList
replicateList = numList * 3
print(concatList)
print(replicateList)

# the del statement will delete values at an index in a list, all the values after the
# deleted value will move up one index
del li[1]
print(li)

# you can replace the range() method in a for loop with a list to loop through the list
for el in li:
    print(el)

# the in and not in operators:
# use these to determine if a value is or isn't in a list
print('dog' in li)
print('cat' in li)
print('pet' not in li)
print('snake' not in li)

# multiple assignment trick (tuple unpacking):
# instead of this:
cat = ['fat', 'gray', 'loud']
catSize = cat[0]
catColor = cat[1]
catDisposition = cat[2]
# write this:
dog = ['small', 'brown', 'energetic']
dogSize, dogColor, dogDisposition = dog
# number of variables and lenght of the list must be exactly equal or you will get a ValueError

# enumerate() function returns the index of the item in the list and the item in the list itself
for index, item in enumerate(li):
    print('Index: ' + str(index) + ' in li is: ' + item)

# random choice and shuffle functions:
import random
food = ['sandwich', 'salad', 'burger', 'BBQ', 'pasta']
# random.choice() randomly selects an item from the list
print(random.choice(food))
print(random.choice(food))
# random.shuffle() randomly reorders the items in a list
print(food)
random.shuffle(food)
print(food)
random.shuffle(food)
print(food)

# index() method is used to get the index of an item, if it is in the list
# if the item is not in the list you will get a ValueError
hello = ['hi', 'hello', 'hey there', 'howdy']
print(hello.index('hi'))
print(hello.index('hey there'))

# add values to a list using append() method
hello.append('hola')
print(hello)
# insert values into a list using insert() method
hello.insert(1, 'yo')
print(hello)
# remove values from the list using remove() method, results in ValueError if item is not in list
hello.remove('hey there')
print(hello)
# sort values in the list using sort() method
unsortedNumbers = [1, 5, -2, 8, 1.5, 9.2]
print(unsortedNumbers)
unsortedNumbers.sort()
print(unsortedNumbers)
unsortedLetters = ['g', 'o', 'a', 't', 'b', 'c']
print(unsortedLetters)
unsortedLetters.sort()
print(unsortedLetters)
# pass True for the reverse keyword to sort in reverse order
unsortedNumbers.sort(reverse=True)
print(unsortedNumbers)
# you cannot sort lists that have both number values and strings in them
# sort uses "ASCIIbetical order", so uppercase letters come before lowercase letters i.e. 'a' comes after 'Z'

# reverse the values in a list with the reverse() method
reverse = [1, 2, 3, 4, 5]
print(reverse)
reverse.reverse()
print(reverse)