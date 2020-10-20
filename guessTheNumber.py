# thiis is a guess the number game to use what I've learned so far.

import random


print('Hello! What is your name?')
name = input()
print('Nice to meet you ' + name + "! I'm thinking of a number between 1 and 20")
secretNumber = random.randint(1, 20)


for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break


if guess == secretNumber:
    print('Good job! You guessed the number in ' + str(guessesTaken) + ' guesses')
else:
    print('No the number I was thinking of was ' + str(secretNumber) + ', Sorry!')

