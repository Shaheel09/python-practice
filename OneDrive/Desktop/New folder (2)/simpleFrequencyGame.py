count = {}

for i in range(5):
    userInput = input('Enter a word: ')
    userInput = userInput.split()

    for s in userInput:
        count.setdefault(s, 0)    
        count[s] += 1

print(count)