# this is a practice project that explores the Collatz sequence

import time

# collatz function definition
def collatz(number):
    if (number % 2) == 0: # check if number is even
        print(number // 2)
        return number // 2
    else: # number is odd
        print(3 * number + 1)
        return 3 * number + 1

# user input loop
while True:
    print('Enter an integer:')
    try:
        userNumber = int(input()) # get integer input
        break # break out of input loop
    except ValueError:
        print('Invalid argument.')


# output loop
while userNumber != 1:
    userNumber = collatz(userNumber) # change the value of userNumber
    time.sleep(0.1) # pause for 1/10 of a second just for effect