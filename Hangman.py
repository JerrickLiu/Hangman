import time

word = 'hangman'

turns = 5

guesses = ''

failures = 0

while turns > 0:

    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failures += 1

    if failures == 0:
        print('You won')
        break

    guess = input('Guess a letter: ')

    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong')
        print('You have ' + str(turns), 'more guesses')

        if turns == 0:
            print('You lose')






