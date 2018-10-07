inventory = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12, "sword": 3}

def display_inventory(stuff):
    print ("Inventory:")
    total_inventory = 0
    for k, v in stuff.items():
        print (str(v) + " " + k)
        total_inventory += v
    print ("Total number of items: " + str(total_inventory))

display_inventory (inventory)
