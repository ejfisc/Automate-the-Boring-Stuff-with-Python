# rock, paper, scissors game
import random, sys # import random and sys modules

print('ROCK, PAPER, SCISSORS') # game title

# game data
wins = 0
losses = 0
ties = 0

while True: # main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties)) # reference variables inside a string
    while True: # player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # quit the game
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # break out of the player input loop
        print('Type one of r, p, s, or q.')

    # display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses += 1



        