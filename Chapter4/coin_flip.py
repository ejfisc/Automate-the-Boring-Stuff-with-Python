import random

numberOfStreak = 0
coin = ['H', 'T']

for experimentNumber in range(10000):
    # create a list of 100 heads or tails values
    flips = []
    for i in range(100):
        flips.append(random.choice(coin))

    # check if there is a streak of 6 heads or tails in a row
    currentStreak = flips[0]
    numberOfFlips = 0
    for flip in flips:
        # check for new streak
        if numberOfFlips == 0:
            currentStreak = flip
        # check if same flip
        if flip == currentStreak:
            numberOfFlips += 1
        else:
            currentStreak = flip
        #check if 6 streak
        if numberOfFlips == 6:
            numberOfStreak += 1
            numberOfFlips = 0

print('Chance of streak: %s%%' % (numberOfStreak / 10000))
        
