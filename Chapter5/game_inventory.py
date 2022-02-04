# in a video game, a player's inventory is represented using a dictionary, each key is the item
# description, and each value is how many of that key the player has
# game_inventory.py contains the displayInventory() method which prints out the inventory in a neat manner
# and addToInventory, which takes a list of items, and adds them to the player's inventory

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# function to display inventory
def displayInventory(inventory):
    print('Inventory:')
    totalItems = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        totalItems += v
    print('Total number of items: ' + str(totalItems))

# function to add to inventory
def addToInventory(inventory, loot):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1
        print(item + ' added to inventory.')
    displayInventory(inventory)

displayInventory(inventory)
addToInventory(inventory, dragonLoot)
