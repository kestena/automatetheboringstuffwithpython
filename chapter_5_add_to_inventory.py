def add_to_inventory (inventory, added_items):
    for i in range(len(added_items)):
        inventory.setdefault(added_items[i], 0)
        inventory[added_items[i]] += 1
    return inventory
    
def display_inventory (display):
    print ("Inventory:")
    total_inv = 0
    for k, v in display.items():
        print (str(v) + " " + k)
        total_inv += v
    print ("Total number of items: " + str(total_inv))
    
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory (inv, dragonLoot)
display_inventory (inv)
