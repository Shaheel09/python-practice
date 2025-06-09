import random

print('THIS IS THE NUMBER GUESSING GAME. \n PLEASE ENJOY THIS GAME')

actualNumber = random.randint(1,20)

def guessNumber():
    attempts = 0
    while attempts < 7:
        guess = int(input('Enter your guess(1-20) : '))
        attempts = attempts + 1
        
        if guess == actualNumber:
            print(f'You\'ve guessed the correct number {actualNumber} in {attempts} attempts!')
        elif guess < actualNumber:
            print('You guessed too low.')
        else:
            print('Too high. Try again')

    print('Sorry, you used all your 7 attempts. The correct number was',actualNumber)

guessNumber()
