# this program creates a small back and forth zig zag animation until the user stops it
# by hitting the editor's stop button or pressing the stop command or ctrl-c

import time, sys

indent = 0 # how many spaces to indent
indentIncreasing = True # whether the indentation is increasing or not

try:
    while True: # the main program loop
        print(' ' * indent, end='') # print indent spaces with no newline character
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second, this gives it the 'animation'
        if indentIncreasing: # i.e. if indentIncreasing == True
            # increase the numer of spaces
            indent += 1
            if indent == 20:
                # change direction
                indentIncreasing = False
        else:
            # decrease the number of spaces:
            indent -= 1
            if indent == 0:
                # change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit() # exit the program upon keyboard interrupt error (if the user hits ctrl-c)