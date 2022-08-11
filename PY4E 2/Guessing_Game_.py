#Guess a Number between 1 and 47:
import random

number = random.randrange(1,47)
Userguess = int(input('Guess a number between 1 and 47: '))

while Userguess != number:
    if Userguess < number:
        print("You need to guess higher. Try again")
        Userguess = int(input('Guess a number between 1 and 47:'))
    else:
        print("You need to guess lower.Try again")
        Userguess = int(input('Guess a number between 1 and 47:'))

print('You guessed the number correctly!')
