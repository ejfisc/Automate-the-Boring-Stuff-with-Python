#! python3
# idiot.py - simple program that uses input validation to repeatedly ask the user if they'd like to know how 
# to keep an idiot busy for hours. If the user answers no, quit. If the user answers yes, go back to step 1.

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    # it is useful to note that inputYesNo() also takes input such as 'y' or 'n' and isn't case-sensitive
    # the inputYesNo function will return 'yes' or 'no' depending on the user's input
    if response == 'no':
        break

print('Ok, in spanish this time.')

while True:
    prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
    response = pyip.inputYesNo(prompt, yesVal='sí', noVal='no')
    # you can use yesVal and noVal to specify what constitutes as yes and no
    if response == 'no':
        break

print('Fine, have a nice day.')