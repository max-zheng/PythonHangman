import sys
from hangman import Hangman
game = Hangman()
word = raw_input("Hello player 1: please enter a word for the other player to guess -> ")
game.word = word
game.setcorrect()
print game.correct

def setguess():
    try:
        num = int(raw_input("Please enter the number of incorrect guesses you would like to give player 2 -> "))
        return num
    except ValueError:
        print "Please enter an integer."
        setguess()

num_guess = setguess()

raw_input("Press enter and hand the computer to player 2")
print ".\n.\n.\n.\n.\n.\n.\n.\n" * 5

print "Welcome to hangman! A word has been entered. You have %d guesses to guess the word. Good luck!" % num_guess

def guess():
    try:
        g = str(raw_input("\nPlease enter a letter to guess -> "))
        if len(g) != 1:
            "Please enter one letter"
            guess()
        game.guessed.append(g)
        return g
    except ValueError:
        print "Please enter one letter."
        guess()

while num_guess > 0:
    the_guess = guess()
    a = game.compare(the_guess)
    if a == False:
        num_guess -= 1
    game.printguessed()
    game.checkwin()

game.losemessage()
quit(0)
