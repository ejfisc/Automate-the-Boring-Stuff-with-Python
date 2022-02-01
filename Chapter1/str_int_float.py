# the str() function takes an integer or floating-point value and converts it to a string
print(str(29)) # evaluates to '29'
print(str(-3.14)) #evaluates to '-3.14'

# the int() function converts the value it is given to an integer
print(int(1.25)) # int() rounds floating-point numbers down, this evaluates to 1
print(int('101')) # evaluates to 101
# these will display an error
# int('99.99') or int('twelve')

# the float() function converts the value it is given to a floating-point number
print(float('3.14')) # evaluates to 3.14
print(float(10)) # evaluates to 10.0

# equivalence

print(42 == '42') # evaluates to false
print(42.0 == '42.0') # evaluates to false
print(42 == 42.0) # evaluates to true

# python makes this distinction because strings are text while integers and floats are both numbers

