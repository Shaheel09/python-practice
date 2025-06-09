inventory = {'apple': 2, 'banana': 5, 'orange': 1}

def invent(stuff):

    for s in range(5):
        userInput = input('Enter an item to add to inventory: ')
        
        if userInput not in stuff:
            stuff.setdefault(userInput, 0)
            stuff[userInput] = inventory[userInput] + 1
        else:
            stuff[userInput] += 1

    return stuff    
    
invent(inventory)
print(inventory)