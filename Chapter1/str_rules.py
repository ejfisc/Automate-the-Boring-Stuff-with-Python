# string concatenation and replication

# when + is used on two string values, it joins the strings as the string concatenation operator
print('Alice' + 'Bob') # evaluates to 'AliceBob'

# this will display an error message because python does not automatically convert the integer to a string
# print('Alice' + 42) 

# you can replicate a string using * 
print('Alice' * 5) # evaluates to 'AliceAliceAliceAliceAlice'
# that only works with integer values, 'Alice' * 5.0 will result in an error

# this will be an error because you cannot multiply two string values
# print('Alice' * 'Bob')