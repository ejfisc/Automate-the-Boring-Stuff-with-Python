# None keyword is the python equivalent of Null

def noReturn():
    print('This function has no return value, so Python automatically adds \'return None\' to the end')

var = noReturn()
print(None == var) # evaluates to true

# keyword arguments in the print() function

# the end keyword changes the newline character to a different string
print('Hello', end='')
print('World')
# prints HelloWorld

# passing multiple strings to print() separates them with a single space
print('python', 'is', 'cool')
# prints python is cool
# use the sep keyword to change that separation character
print('dogs', 'cats', 'fish', sep=',')
# prints dogs,cats,fish

