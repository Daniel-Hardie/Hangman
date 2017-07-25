import random      #importing the random module from the python archives
import time        #importing the time module from the python archives
wordList = ["cars", "pear", "jazz", "halo", "flip", "pipes", "pizza", "grape", "banjo", "wheel",
            "atomic", "galaxy", "sphinx", "oxygen", "chisel", "croquet", "buffalo", "whistle", "numeric", "crafted"]    #List of words hard coded in my program
def letterGuess(letter):
    userGuess=input("Please enter a letter ")
    userGuess=userGuess.lower()
    while len(userGuess)>1:
        userGuess=input("Please enter only one letter. Try again.\nPlease enter a letter")
    while userGuess not in 'abcdefghijklmnopqrstuvwxyz':
        userGuess=input("Please only enter a letter!\nPlease enter a letter ")
    while userGuess in guesses:
        userGuess=input("You have already guessed that letter!\nPlease enter a letter ")
    return userGuess    
def wordConvert(letter):
    for i in range(len(wordToGuess)):
        if wordToGuess[i] == letter:
            uncovering[i]=letter
print("HANGMAN\n\nHello and welcome to hangman! To win this game, all you have to do is to guess\nall of the letters in "
      "the word. Try not to get too many incorrect guesses or\notherwise you will lose.  Good luck!\n")
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
    print("Get ready for game", roundNumber, "\n")
    time.sleep(1)
    rand=random.randrange(0, len(wordList)-1)
    wordToGuess=wordList[rand]
    uncovering=[]
    incorrectGuessRem=8
    guesses=[]
    for letter in range(len(wordToGuess)):
        uncovering+=["_"]
    while "_" in uncovering and incorrectGuessRem>0:
        print("Incorrect Guesses Remaining:", incorrectGuessRem)
        for i in uncovering:
            print(', '.join(str(item) for item in i), end=" ")
        print()
        print("Letters guessed:", end='')
        for i in guesses:
            print(', '.join(str(item) for item in i), end=" ")
        print()
        userGuess=str(input)
        print(letterGuess(userGuess))
        guesses+=[userGuess]
        print()
        if userGuess in wordToGuess:
            wordToGuess=wordConvert(userGuess)
        else:
            incorrectGuessRem-=1
            print("Sorry the letter you guessed is not in the word.")
        print()
    if incorrectGuessRem==0:
        print("Sorry but you have run out of guesses! The word you were trying to guess was", wordToGuess)
        print()
        roundNumber+=1
        numbGames-=1
    else:
        print("Congratulations you won!  The Word you guessed was", wordToGuess)
        print()
        roundNumber+=1
        numbGames-=1
