class Hangman(object):

    def __init__(self):
        self.word = ""
        self.correct = []
        self.guessed = []

    def setcorrect(self):
        i = 0
        while i < len(self.word):
            self.correct.append("_")
            i += 1

    def compare(self, guess):
        success = False
        split = list(self.word)
        i = 0
        while i < len(split):
            if split[i] == guess:
                self.correct[i] = guess
                success = True
            i += 1
        if success == False:
            print "Sorry! You guessed incorrectly."
        else:
            print "Good job! Here are the letters you guessed correctly."

        self.display()

        if success == False:
            return False
        else:
            return True


    def checkwin(self):
        won = True
        split = list(self.word)
        i = 0
        while i < len(self.word):
            if split[i] != self.correct[i]:
                won = False
            i += 1

        if won == True:
            print "Congrats! You won!"
            quit(0)
        else:
            return

    def losemessage(self):
        print "Sorry! You lost! Better luck next time!"

    def display(self):
        i = 0
        while i < len(self.correct):
            print "%s " % self.correct[i],
            i += 1

    def printguessed(self):
        print "Here are the letters you have guessed already: ",
        for j in self.guessed:
            print j + " ",
