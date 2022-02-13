#! python3
# multiplication_quiz.py - poses random multiplication problems for the user and times their response

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # pick two random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        # right answers are handled by allowRegexes
        # wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], # allows only the sum
                              blockRegexes=[('.*', 'Incorrect!')], # if wrong answer, 'Incorrect' is displayed and the user is promped to answer again
                              timeout=8, limit=3) # ensures the user only has 8 seconds and 3 attempts to answer
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # this block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers += 1

    time.sleep(1) # brief pause to let user see the result

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
    