from decimal import ConversionSyntax
import re
# passing a string to re.compile() returns a regex pattern object
# \d means 'a digit character' and \d\d\d-\d\d\d-\d\d\d\d is the regular expression (regex)
# for a phone number pattern. \d{3}-\d{3}-\d{4} also works
# put a 'r' before the string to signify a raw string
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 512-920-8983')
print('Phone number found: ' + mo.group())

# you can use parentheses to create groups in the regex
# for example, you can use parentheses to  separate the area code from the phone number
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 512-920-8983')
print(mo.group(1)) # '512'
print(mo.group(2)) # '920-8983'
print(mo.group(0)) # '512-920-8983'
print(mo.group()) # same as group(0)
print(mo.groups()) # ('512', '920-8983')

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# . ^ * + ? { } [ ] \ | ( ) all have special meaning in regex, if you want to detect
# these characters as part of your text pattern, you need to escape them with a backslash
# for example: (xxx) xxx-xxxx
phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is (512) 920-8983')
print(mo.groups())
print(mo.group())

# the | character is called a pipe, allows you to match multiple expressions
# the following expression will match either 'Batman' or 'Tina Fey'
# if both show up in the same text, the first occurence will be returned
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group()) 
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
# you can use parentheses with the pipe to match specific patterns
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# you can use the question mark to mark a group as optional, meaning the regex should
# find a match regardless of whether that bit of text is there
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

# you can use the star to mean 'match zero or more', meaning the regex should find a match
# if that text shows up any number of times
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowoman')
print(mo3.group())

# you can use the plus to mean 'match one or more' meaning the regex should find a match
# if that text shows up at least once 
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batman') 
print(mo1 == None)
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowoman')
print(mo3.group())

# you can use braces to match repeat phrases
haRegex = re.compile(r'(Ha){3}') # will match with 'HaHaHa'
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)
# you can specify a range by writing minimum, maximum or by leaving out the 1st or 2nd number
haRegex = re.compile(r'(Ha){3,5}') # matches to 3, 4 or 5 instances of Ha
haRegex = re.compile(r'(Ha){,5}') # matches to 0..5 instances of Ha
haRegex = re.compile(r'(Ha){3,}') # matches to 3 or more instances of Ha
# given the choice, Python will match to the longest string possible (greedy matching)
# you can indicate non-greedy (lazy) matching with a question mark after the braces
mo = haRegex.search('HaHaHaHaHaHa')
print(mo.group())
haRegex = re.compile(r'(Ha){3,5}?')
mo = haRegex.search('HaHaHaHaHa')
print(mo.group())

# regex objects also have the findall() method which returns a list of every match
# as long as there are not groups in the regex
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)
# if there are groups in the regex, findall() will return a list of tuples where each tuple
# represents a found match, and its items are the matched strings for each group in the regex
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

# shorthand character classes:
# \d - any numeric digit from 0 to 9
# \D - any character that is not a numeric digit from 0 to 9
# \w - Any letter, numeric digit, or the underscore character
# \W - any character that is not a letter, numeric digit, or the underscore character
# \s - any space, tab, or newline character
# \S - any character that is not a space, tab or newline

# these are useful for shortening regex. The character class [0-5] will 
# match numbers from 0 to 5, and is much shorter than typing (0|1|2|3|4|5)
# there is no shorthand class that matches only letters, but you can use [a-zA-Z] class

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# you can define your own character class using the square brackets
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
letNumRegex = re.compile(r'[a-zA-Z0-9]') # will match all lowercase and uppercase letters, and numbers
# note that inside square brackets you dont need to escape meaningul symbols
# the character class [0-5.] will match digits 0-5 and a period, no need to write it as [0-5\.]

# by placing a caret character just after the class opening bracket, you can make a negative character class
# a negative character class will match all the characters that are not in the class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# the ^ can also be used at the start of a regex to indicate that a match must occur
# at the beginning of the searched text
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello, world!'))
print(beginsWithHello.search('He said Hello.'))

# the $ can be used at the end of a regex to indicate that a match must occur
# at the end of the searched text
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('42 is your number'))

# you can use multiple special characters to be even more specific
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890')) # match
print(wholeStringIsNum.search('123abc456')) # none
print(wholeStringIsNum.search('123 456')) # none

# the . character in a regex is called a wildcard and will match any character except newline
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
# the . character only matches one character. To match an actual dot, escape the . with a backslash

# you can use .* to match anything and everything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Ethan Last Name: Fischer')
print(mo.group(1)) # 'Ethan'
print(mo.group(2)) # 'Fischer'
# the .* uses greedy matching, to match any text in a non-greedy fashion, use .*?
nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) # '<To serve man>'
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# technically, .* will match everything except a newline, but if you want to include newline,
# pass re.DOTALL as the second argument to re.compile()
noNewLineRegex = re.compile(r'.*')
mo = noNewLineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the law.')
print(mo.group())
newLineRegex = re.compile(r'.*', re.DOTALL)
mo = newLineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the law.')
print(mo.group())

# by default, regex are case sensitive
# you can pass re.IGNORECASE or re.I as a second argument to re.compile() to match the letters regardless of case
robocop = re.compile(r'robocop', re.I)
print(robocop.search('robocop').group())
print(robocop.search('RoBoCoP').group())
print(robocop.search('ROBOCOP').group())

# the sub() method can substitute new text in place of matched regex patterns
# sub() is passed 2 arguments, a string to replace any matches, and a string for the regex
# the sub() method returns a string with the substitutions applied
namesRegex = re.compile(r'Agent \w+')
censored = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(censored)
# you may need to use the matched text itself as part of the substitution. In the first argument to sub, you can
# type \1, \2, \3 and so on to mean 'Enter the text of group 1, 2, 3 and so on in the substitution'
# i.e. let's say you want to censor the names of the secret agents by showing just the first letters of their names
# use the regex Agent (\w)\w* and pass r'\1****' as the first argument to sub()
agentNamesRegex = re.compile(r'Agent (\w)\w*')
censored = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(censored)

# matching complicated text patterns might require long, convoluted regex. You can mitigate this by telling
# re.compile() to ignore whitespace and comments inside the expression string (verbose mode)
# by passing re.VERBOSE as the second argument to re.compile()
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)

# if you want to combine re.IGNORECASE, re.DOTALL, and re.VERBOSE, re.compile() only takes 2 arguments
# but you can use | (in this context it is the bitwise or operator)
# so if you want a regex that's case sensitive and includes newlines to match the dot character:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
# including all 3:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
