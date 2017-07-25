import random      #importing the random module from the python archives
import time        #importing the time module from the python archives

wordList = ["cars", "pear", "jazz", "halo", "flip", "pipes", "pizza", "grape", "banjo", "wheel",
            "atomic", "galaxy", "sphinx", "oxygen", "chisel", "croquet", "buffalo", "whistle", "numeric", "crafted"]    #List of words hard coded in my program

def chooseRandomWord(wordList):
    i = random.randrange(0, len(wordList)-1)  
    return wordList[i]

def letterGuess(letter):
    while True:
        global userGuess
        userGuess=input("Please enter a letter ")
        userGuess=userGuess.lower()
        if len(userGuess)>1:
            print("Please enter only one letter. Try again.")
        elif userGuess not in 'qwertyuiopasdfghjklzxcvbnm':
            print("Please enter a letter!")
        elif userGuess in letter:
            print("You have already guessed that letter! Try again.")
        else:
            return userGuess
    
print("HANGMAN\nHello and welcome to hangman! To win this game, all you have to do is to guess\nall of the letters in "
      "the word. Try not to get too many incorrect guesses or\notherwise you will lose.  Good luck!")

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
    wordToGuess=chooseRandomWord(wordList)
    incorrectGuessRem=8
    incorrectLetters=''
    wordGuessed=False
    print("Get ready for game", roundNumber)
    time.sleep(1)
    while wordGuessed is False:
        print("Incorrect guesses remaining:", incorrectGuessRem)
        print("Incorrect letters guessed:", incorrectLetters)

for char in word:      
        if char in guesses:    
        # print then out the character
            print(char),    
        else:
        # if not found, print a dash
            print("_")

        wordGuessed=True
    else:
        print("Congratulations you won!  The Word you guessed was", wordToGuess)
        numbGames-=1
        roundNumber+=1


'''
look at boolean return modules
'''


