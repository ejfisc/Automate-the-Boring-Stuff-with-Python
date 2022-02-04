import copy
# copy.copy() can be used to make a duplicate copy of a mutable value like a list, not just
# a copy of a reference
spam = ['A', 'B', 'C', 'D']
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese)) # cheese is a different list with a different identity
cheese[1] = 42
print(spam)
print(cheese) 

# if the list you need to copy contains lists, use copy.deepcopy() instead, this will copy the
# inner lists as well