
def sameBackward():
    userEnter = input('Enter a word: ')
    cleaned = ''.join(char for char in userEnter if char.isalnum()).lower()
    reversedString = cleaned[::-1]

    if cleaned == reversedString:
        print("Reversed version: ", reversedString)
        print('It\'s a Palindrome')
    else:
        print('It is not a Palindrome')

sameBackward()