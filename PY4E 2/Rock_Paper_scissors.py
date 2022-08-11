#Guess a Number between 1 and 47:
import random

def GenerateRandomNumber():
    RandomNumber= rnadom.randint( 1, 3)
    return GenerateRandomNumber

def getConmputerChoice( randomNumber):
    if randomNumber == 3:
        computerChoice = 'rock'
    elif randomNumber == 2:
        computerChoice = 'paper'
    elif randomNumber == 3:
        computerChoice = 'scissors'

    return computerChoices

    def getUserChoice():
        userChoice = input( 'Please enter your choice')
        return userChoice

    def DetermineWinner( computerChoice, userChoice):

        rockMessage =  'The rock smashes the scissors'
        scissorsMessage = 'Scissors cuts paper'
        paperMessage = 'Paper wraps rock'

        if computerChoice == 'rock' and userChoice == 'scissors':
            winner = 'Computer'
            message = rockMessage
        elif computerChoice == 'Scissors' and userChoice == 'rock':
            winner = 'You'
            message = rockMessage

        if computerChoice == 'scissors' and userChoice == 'paper':
            winner = 'Computer'
            message = scissorsMessage
        elif computerChoice == 'paper' and userChoice == 'scissors':
            winner = 'You'
            message = scissorMessage

        if computeChoice == 'paper' and userChoice == 'rock':
            winner = 'Computer'
            message = paperMessage

        return winner , message

    def main():
        randomNumber = generateRandomNumber()
        computerChoice = getComputerChoice( random number )
        userChoice = getUserChoice()
        print()
        print( 'The computer chose' computersChoice )
        winner, message = DetermineWinner( computerChoice, userChoice)

        if winner != 'no winner'
            print( winner, 'won(', message, ')' )

        while winner == 'no winner':
            print( '\nYou both chose the same thing' )

main()




        #remeber to compare rock paper and scissors/ possibly make them different variables
        # express rock paper and scirssors through text (using if)
