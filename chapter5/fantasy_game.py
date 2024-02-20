
# We want a function to print a user's inventory
def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(f'{v}\t{k}')
        item_total += v
    print(f'Total inventory items: {item_total}')


def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] += 1


joe_items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(joe_items)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print('After conquering the dragon\n')
addToInventory(joe_items, dragonLoot)
display_inventory(joe_items)
