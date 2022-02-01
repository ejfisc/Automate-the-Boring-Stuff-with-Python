# if statements consist of 4 components:
# the if keyword, a condition, a colon, and the if clause

# variables for later
name = 'Bob'
age = 10

if name == 'Alice':
    print('Hi, Alice.')

# else statements consist of the else keyword, a colon and the else clause

if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')

# elif (else if) statements are structured the same as the if statements but come after 
# an original if statement

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')

# while loops consist of the while keyword, a condition, a colon, and the while clause

#this example prints 'Hello, world.' 5 times
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# break statements are used to break out of a while loop's clause early

countDown = 10
while countDown > 0:
    print(countDown)
    if countDown == 3:
        print('Timer Broke!')
        break
    countDown = countDown - 1

# look at password.py for a continue statement example

# a for loop uses the for keyword, a variable name, the in keyword, a call to the range() method,
# a colon and the for clause
# break and continue statements can be used in for loops as well

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# the range() function can be called with up to 3 arguments
# when called with 1 argument x, range will start at 0 and go up to x - 1, iterating x times

# this loop will print 0, 1, 2, ... 9
for i in range(10):
    print(i)

# when called with 2 arguments x, y, range will start at x and go up to y - 1, iterating y - x times

# this loop will print 12, 13, 14, 15
for i in range(12, 16):
    print(i)

# when called with 3 arguments x, y, and z, range will start at x and go up to y in intervals of z

# this loop will print 0, 2, 4, ... 8
for i in range(0, 10, 2):
    print(i)

# you can use a negative number for the step argument to make the for loop count down instead of up

# this loop will print 5, 4, 3, ... 0
for i in range(5, -1, -1):
    print(i)
