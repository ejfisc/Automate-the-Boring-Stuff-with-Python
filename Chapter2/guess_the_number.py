# this is a guess the number game
import random # import the random module

number = random.randint(1, 20) # get the secret random number

print('I am thinking of a number between 1 and 20')
print('You get 6 guesses')

# loop 6 times

for guesses in range(1, 7):
    print('Take a guess.')
    guess = int(input()) # you can get integer inputs by using passing input() to the int() function
    if guess == number:
        break # correct guess
    elif guess > number:
        print('Your guess is too high.')
    elif guess < number:
        print('Your guess is too low.')
        
if guess == number:
    print('Good job! You guessed my number in ' + str(guesses) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(number))