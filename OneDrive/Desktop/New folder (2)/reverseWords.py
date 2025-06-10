userEnter = input('Enter a sentence: ')

words = userEnter.split()
words.reverse()
words = ' '.join(words)

print(words)