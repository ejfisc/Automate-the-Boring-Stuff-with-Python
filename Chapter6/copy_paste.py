# you can use the pyperclip module to copy and paste text from the clipboard
import pyperclip as pclip
# pclip.copy('Hello, World!')
print(pclip.paste())
# if you copy something else to the clipboard and call paste(), like this sentence for example,
# that is what will show up
print(pclip.paste())