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

