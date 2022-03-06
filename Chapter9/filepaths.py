# you can use Path objects from the pathlib module to help work with file path names
from pathlib import Path
import sys

# The Path() function returns a WindowsPath or PosixPath object depending on your operating system
# windows file paths use backslashes, (ex: C:\Users\...) linux/macOS file paths use forward slashes (ex: /usr/bin/...)

print(Path('/', 'Users', 'ethanfischer', 'Documents', 'GitHub', 'Automate-the-Boring-Stuff-with-Python'))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path('/User/Documents', filename))

# just as we can use + to join integers or strings, we can use / to join path objects
print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon', 'eggs'))
# when using / to join path objects, either the first or second left most object must be a path object

# you can get the cwd as a string value using Path.cwd() and change it using os.chdir()
import os
print(Path.cwd())
os.chdir('/Users/ethanfischer/Documents/school')
print(Path.cwd())
# changing the cwd while a program is running can cause bugs, be careful with this

# every user has a home directory their files are under
# you can get the path of the home folder by calling Path.home()
print(Path.home())
# in windows, the home directories are under C:\Users
# in macOS, the home directories are under /Users
# in Linux, the home directories are under /home
# your scripts will almost certainly have permissions to read and write the files under your home directory, so that 
# is an ideal place to put the files that your program will work with.

# An absolute path for a file always begins with the root directory
# a relative path for a file is relative to the current working directory
# . is shorthand for this directory, .. is shorthand for parent directory
# is_absolute() will return true if a path object represents an absolute path or false if it represents a relative path
print(Path.cwd().is_absolute())
print(Path('../Chapter6').is_absolute())

# you can use os.makedirs() to create a new directory including any subdirectories
os.chdir('../GitHub/Automate-the-Boring-Stuff-with-Python/Chapter9')
os.makedirs('./new directory/new subdirectory')
# you can call .mkdir() on a path object to create one single directory
Path('./new directory 2').mkdir()
