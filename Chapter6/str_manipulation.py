# strings can begin and end with double quotes too, this allows your string to have a single quote 


print("This is Alice's cat.") # python would assume your string had ended otherwise
# if you need to use both in any situation, you can use escape characters
print('This is Alice\'s cat.') # this also works though
print("\"This is a famous quote from a real person.\"")

# escape characters begin with \:
print('\'') # single quote
print("\"") # double quote
print('tab \t tab') # tab
print('newline\n') # newline
print('\\') # backslash

# raw strings ignore escape characters and prints any backslash that appears in the string
# place an r before the beginning of a string to mark it raw
print(r'That is carol\'s cat.') # prints 'That is carol\'s cat.'
# raw strings are helpful for strings used for file paths like 
print(r'C:\Users\Ethan\Desktop')

# triple quotes:
# you can use three single quotes or double qoutes to indicate a multiline string
# any quotes, tabs or newlines in between the triple quotes are considered part of the string
# python's indentation rules for blocks do not apply to multiline strings
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

# multiline strings are often used for comments that span multiple lines, this is perfectly valid python code:
"""This is a test python program
Written by Ethan Fischer ejfisc@protonmail.com
This is a multiline comment to show that triple
quote multiline strings can be used as comments"""

# you can use indexes and slice strings just like lists
hello = 'Hello, World!'
print(hello[0]) # 'H'
print(hello[4]) # 'o'
print(hello[-1]) # '!'
print(hello[:5]) # 'Hello'
print(hello[7:]) # 'World!'
# note that slicing does not modify the string
world = hello[7:]
print(world, hello)

# the in and not in operators work with strings too
print('Hello' in hello) # true
print('abc' not in world) # true
print('Hello' in world) # false

# string interpolation:
# the %s operator inside the string acts as a marker to be replaced by values following the string
name = 'Ethan'
age = 20
print('My name is %s. I am %s years old.' % (name, age))

# python 3.6 introduced f-strings, which is similar to string interpolation but braces
# are used instead of the %s operator, with expressions placed directly inside the braces
# similar to marking raw strings, place an 'f' before the beginning of the string
print(f'My name is {name}. Next year I will be {age + 1}.')

# the upper() and lower() methods return a new string where all the letters in the original
# string have been converted to uppercase or lowercase letters respectively
print(hello.upper(), hello.lower())
# these methods do not change the string itself but return new strings
# these methods are helpful if you need to make a case sensitive comparison

# the isupper() and islower() methods return True if the string has at least one letter
# and all the letters are uppercase or lowercase respectively, otherwise False.
print(hello.isupper(), hello.islower())
hello = hello.upper()
print(hello.isupper())
print('abc12345'.islower())
print('12345'.islower())

# the isalpha() method returns true if the string consists only of letters and isn't blank
print('sdflkjsd'.isalpha(), 'I am 20'.isalpha())
# the isalnum() method returns true if the string consists only of letters and numbers and isn't blank
print('let134'.isalnum(), 'Hi, there.'.isalnum())
# the isdecimal() returns true if the string only consists of numeric characters and isn't blank
print('It is 9:51'.isdecimal(), '2022'.isdecimal())
# the isspace() method returns true if the string consists only of spaces, tabs and newlines and isn't blank
print(''.isspace(), '    '.isspace(), 'There are spaces in this string'.isspace())
# the istitle() method returns true if the string consists of words that begin with an uppercase
# letter followed by only lowercase letters
print('This Is A Title'.istitle(), 'tHis Is nOt A tiTle'.istitle())

# the startswith() and endswith() methods return True if the string value begins or ends respectively
# with the string passed to the method
utd = 'University of Texas at Dallas'
print(utd.startswith('University'), utd.endswith('Dallas'))
print(utd.startswith('The'), utd.endswith('D'))
# these methods are useful alternatives to the == operator if you need to check only whether the 
# first or last part of the string is equal to another string

# the join() method is useful when you have a list of strings that need to be joined 
# together into a single string value, it works like this:
print(', '.join(['cats', 'rats', 'bats'])) # prints cats, rats, bats
print(' '.join(['My', 'name', 'is', 'Ethan'])) # prints My name is Ethan
print('ABC'.join(['My', 'name', 'is', 'Ethan'])) # prints MyABCnameABCisABCEthan

# the split() method splits a string into a list, by default the string is split wherever
# there is whitespace such as spaces, tabs or newlines. You can pass a delimiter string to the
# split() method to specify a different string to split upon
utd.split()
print(utd.split())
print(utd.split('t'))
# you could also split a multine string along the newlines
letter = '''Dear reader,
This is a sample multiline string
for the purposes of demonstrating
the use cases for the python
split() string method.
Sincerely,
Ethan.'''
print(letter.split('\n'))

# the partition() method can split a string into the text before and after a separator string
print('Hello, world!'.partition('w'))
print('Hello, world!'.partition('world'))
# if the partition string occurs multiple times in the string, the method splits the string only
# on the first occurence
print('Hello, world!'.partition('o'))
# you can use the multiple assignment trick to assign the 3 returned strings to 3 variables
before, sep, after = 'Hello, world!'.partition(' ')
print(before)
print(after)

# justifying text methods:
# you can use the rjust() and ljust() methods to return a padded version of the string they are called on
# with spaces inserted to justify the text. The first argument to both methods is an integer length 
# for the justified string
print('Hello'.rjust(10)) # prints '          Hello'
print('Hello'.rjust(20)) # prints '               Hello'
print('Hello'.ljust(10)) # prints 'Hello     '
# the integer argument is the total length of the string
print('Hello'.rjust(3)) # an integer value less than the length of the string will just return the string
# an optional second argument will specify a fill character other than a space character
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
# the center() method works like l and rjust() but centers the text
print('Hello'.center(20)) # prints '       Hello        '
print('Hello'.center(20, '='))

# removing whitespace with the xstrip() methods:
# the strip() method will return a new string without any whitespace characters at the beginning or end
helloSpace = '      Hello, World!       '
print(helloSpace.strip())
# the lstrip() and rstrip() methods strip whitespace from the left and right respectively
print(helloSpace.lstrip())
print(helloSpace.rstrip())
# optionally, a string argument will specify which characters on the ends should be stripped
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) # this strips occurences of a, m, p, and capital S from the ends of spam
# the order of the characters in the string passed to strip() does not matter
# strip('ampS') will do the same thing as strip('mapS') or strip('Spam')

# every text character has a corresponding numeric value called a unicode code point
# use the ord() function to get the code point of a one-character string and the chr()
# function to get the one-character string of an integer code point.
print(ord('A'), ord('4'), ord('!')) # note that passing a string longer than 1 character to ord() will result in an error
print(chr(65))
# these functions can be useful when you need to do an ordering or mathematical operation on characters
print(ord('A') < ord('B'))
print(chr(ord('A')))
print(chr(ord('A') + 1))

