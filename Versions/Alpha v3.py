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

def layout(incorrectGuessRem, incorrectLetters, correctLetters, wordToGuess):
    print("Guesses remaining:", incorrectGuessRem)
    print('Incorrect letters:', end=' ')
    for letter in incorrectLetters:
        print(letter, end=' ')
    print()
    unguessedLetters = '_' * len(wordToGuess)
    for i in range(len(wordToGuess)): # replace blanks with correctly guessed letters
        if wordToGuess[i] in correctLetters:
            unguessedLetters = unguessedLetters[:i] + wordToGuess[i] + unguessedLetters[i+1:]
    for letter in unguessedLetters: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()
    
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
    correctLetters=''
    gameFinished=False
    print("Get ready for game", roundNumber)
    time.sleep(1)
    while True:
        layout(incorrectGuessRem, incorrectLetters, correctLetters, wordToGuess)
        userGuess = getGuess(missedLetters + correctLetters)
        if guess in wordToGuess:
            correctLetters = correctLetters + guess
            foundAllLetters = True
            for i in range(len(wordToGuess)):
                if wordToGuess[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == incorrectGuessesRem:
            layout(incorrectGuessRem, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
        if alllettersGuessed:
            print("Congratulations you won!  The Word you guessed was", wordToGuess)
            numbGames-=1
            roundNumber+=1
        else:
            print("Congratulations you lost!  The Word you guessed was", wordToGuess)
            numbGames-=1
            roundNumber+=1


'''
look at boolean return modules
'''


