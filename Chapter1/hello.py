# this program says hello and asks for the user's name

print('Hello, world!')
print('What is your name?')

name = input() # user input is a string value

print('Nice to meet you, ' + name)
print('The length of your name is: ')
print(len(name)) # this uses the len() function which outputs the length of the given string

print('What is your age?') 

age = input()
print('You will be ' + str(int(age) + 1) + ' in a year.')
# convert age to an integer so it can be added to 1, then convert that total value 
# to a string so it can be concatenated to the rest of the print statement
