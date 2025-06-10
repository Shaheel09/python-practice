'''import random

secretNumber = random.randint(1,21)
print('I am thinking of a number between 1 and 20.')

guessTaken = 1

while guessTaken < 7:
    print(secretNumber)
    guess = int(input('Take a guess : '))


    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
    guessTaken = guessTaken + 1

if guess == secretNumber:
    print('Good job! You guessed my number in just ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
  
'''

'''for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
'''

userAge = int(input('Enter Your Age : '))

if userAge <= 12:
    print('You are a Child')
elif userAge >= 13 and userAge <= 19:
    print('You are a Tenager')
elif userAge >= 20 and userAge <= 64:
    print('You are an Adult')
else:
    print('You are a Senior')
