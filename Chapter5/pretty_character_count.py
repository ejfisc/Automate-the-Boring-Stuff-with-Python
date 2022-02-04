import pprint # 'pretty print'
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1
pprint.pprint(count)

# pprint.pprint() prints a clean display of the items in a dictionary