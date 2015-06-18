import sys
import random

def makeYourChoice():
    print "Press R for Rock"
    print "Press P for Paper"
    print "Press S for Scissors"
    print "Press Q to Quit!"


    userChoice = raw_input("What do you choose?").lower()
    if userChoice == "r":
        return "Rock"
    if userChoice == "p":
        return "Paper"
    if userChoice == "s":
        return "Scissors"
    if userChoice == "q":
        sys.exit(0)
    else:
        makeYourChoice()

def computerRandom():
    options = ["Rock","Paper","Scissors"]
    randomChoice = random.randint(0,2)
    return options[randomChoice]

def comparison (playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return "Draw"
    if playerChoice == "Rock" and computerChoice == "Paper":
        return "Computer Wins"
    if playerChoice == "Paper" and computerChoice == "Scissors":
        return "Computer Wins"
    if playerChoice == "Scissors" and computerChoice == "Rock":
        return "Computer Wins"
    else:
        return "Player Wins"

while True:
    playerChoice = makeYourChoice()
    computerChoice = computerRandom()
    print "You chose", playerChoice
    print "The computer chose", computerChoice
    result = comparison (playerChoice, computerChoice)
    if result == "Draw":
        print "It's a draw"
    elif result == "Computer Wins":
        print "Unlucky, you lost!"
    else:
        print "Well done you won!"
    print " "  
