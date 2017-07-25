import random      #importing the random module from the python archives
import time        #importing the time module from the python archives

wordList = ["cars", "pear", "jazz", "halo", "flip", "pipes", "pizza", "grape", "banjo", "wheel",
            "atomic", "galaxy", "sphinx", "oxygen", "chisel", "croquet", "buffalo", "whistle", "numeric", "crafted"]    #List of words hard coded in my program

def letterGuess(letter):
    while True:
        global userGuess
        userGuess=input("Please enter a letter ")
        userGuess=userGuess.lower()
        if len(userGuess)>1:
            print("Please enter only one letter. Try again.")
        elif userGuess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please only enter a letter!")
        elif userGuess in guesses:
            print("You have already guessed that letter! Try again.")
        else:
            return userGuess

def wordConversion(letter):
    for letter in incorrectLetters:
        print(letter, end='')
    print()
    notGuessed='_' * len(wordToGuess)
    for i in range(len(wordToGuess)):
        if wordToGuess[i] in correctLetter:
            notGuessed = notGuessed[:i]+ wordToGuess[i]+ notGuessed[i+1:]
    for letter in notGuessed:
        print(notGuessed, end='')
        print()


print("HANGMAN\n\nHello and welcome to hangman! To win this game, all you have to do is to guess\nall of the letters in "
      "the word. Try not to get too many incorrect guesses or\n\notherwise you will lose.  Good luck!\n")

numbGames=0        #setting the variable for number of games to have a value of 0
while numbGames<1 or numbGames>3:   #while numbGames is less than 1 or greater than 3
    try:       #try block code is executed
        numbGames=int(input("How many games do you want to play? (Up to 3) "))     #setting numbGames variable to user input
        if numbGames<1 or numbGames>3:     #if numbGames value is less than 1 or greater than 3
            print("Please enter a number which is between 1 and 3 ")   #print message
    except ValueError:    #if error in is present for the try block code the except block will be executed instead.
        print("Please enter a number which is between 1 and 3")    #print message

roundNumber=1
while numbGames>0:
    rand=random.randrange(0, len(wordList))
    wordToGuess=wordList[rand]
    incorrectGuessRem=8
    incorrectLetters=[]
    guesses=[]
    print("Get ready for game", roundNumber, "\n")
    time.sleep(1)
    while incorrectGuessRem>0:
        print("Incorrect Guesses remaining:", incorrectGuessRem)
        print("Letters guessed:", incorrectLetters)
        print(wordConversion(wordToGuess), "\n")
        print(letterGuess(userGuess))
        print()
        if userGuess in wordToGuess:
            guesses += userGuess 
        else:
            incorrectGuessRem -= 1
            incorrectLetters += userGuess
            if incorrectGuessRem==0:
                print("Sorry but you have run out of guesses! The word you were trying to guess was", wordToGuess)
                roundNumber += 1
                numbGames -= 1

