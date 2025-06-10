
def countVowels():
    userSentence = input('Enter a sentence to count the vowels: ')
    vowels = 'aeiouAEIOU'
    count = 0

    for letter in userSentence:
        if letter in vowels:
            count += 1
            
    return count

    
result = countVowels()

print('Total vowels are ',result)