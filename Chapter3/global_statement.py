# scope works the same way in python as any other langauge with global and local variables
# if you need to modify a global variable from within a function, use the global statement
# to prevent python from creating a local variable


def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs) # the spam() function changes eggs from 'global' to 'spam', so this prints 'spam'

# another example:

def toast():
    global eggs
    eggs = 'toast' # this is the global variable eggs because there is a global statement for eggs
def bacon():
    eggs = 'bacon' 
    # this is the local variable eggs w/in bacon because there is an assignment statement for eggs
def ham():
    print(eggs) 
    # this is the global variable eggs because there is no global or assignment statement for eggs
eggs = 42 # this is the global variable eggs
toast()
print(eggs) # toast() modifies the global variable eggs, so this prints 'toast'
