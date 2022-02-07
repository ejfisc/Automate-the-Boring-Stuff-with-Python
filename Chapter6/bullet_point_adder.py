#! python3
# bullet_point_adder.py - Adds wikipedia bullet poitns to the start
# of each line of text on the clipboard.
import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n') # get a list of each line in the clipboard
for i in range(len(lines)): # loop through all indexes in the lines list
    lines[i] = '* ' + lines[i] # add a start to each string in the lines list

# Join the modified lines
text = '\n'.join(lines)

pyperclip.copy(text)