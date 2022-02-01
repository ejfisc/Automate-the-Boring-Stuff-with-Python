# uses the break and continue statements inside a while loop to check for valid user 'Joe'

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue # jump back to start, i.e. user must reenter a name until they enter the name 'Joe'
    print('Hello, Joe. What is the password? (Hint: It is a fish.)')
    password = input()
    if password == 'swordfish':
        break # correct password, exit the loop
    else:
        print('Incorrect password.') # incorrect password, goes back to beginning

print('Access granted.')