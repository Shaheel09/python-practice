userSentence = input('Enter a setence: ')
userLetter = input('Enter a letter to count: ')

count = 0

for letter in userSentence:
    if letter.lower() == userLetter.lower():
        count+= 1 

print(count)
