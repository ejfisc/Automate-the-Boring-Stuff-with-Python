#! python3
# mclip.py - A multi-clipboard program.
import sys, pyperclip

TEXT = {'agree': '''Yes, I agree. That sounds fine to me.''',
        'busy': '''Sorry, can we do this later this week or next week?''',
        'upsell': '''Would you consider making this a monthly donation?'''}

# command line arguments are stored in the list sys.argv. The first item should always be a string
# containing the program's filename ('mclip.py'), and the seond item should be the first
# command line argument.
# check that the user entered a command line argument:
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line argument is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)