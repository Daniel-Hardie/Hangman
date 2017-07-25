import random      #importing the random library from the python archives
import time        #importing the time library from the python archives


wordList = ["cars", "pear", "jazz", "halo", "flip", "pipes", "pizza", "grape", "banjo", "wheel", "rope", "picture", "shown", "throw", "ticket", "square", "table",
            "chef", "atomic", "galaxy", "sphinx", "oxygen", "chisel", "croquet", "buffalo", "whistle", "numeric", "crafted"]    #List of words hard coded in my program

def letterGuess(letter):   #defining the letterGuess module
    global userGuess   #setting the userGuess variable to global
    while len(userGuess)>1 or userGuess not in 'abcdefghijklmnopqrstuvwxyz' or userGuess=='' or userGuess in guesses:  #while character input is larger than one character or not in the alphabet or is nothing or has already been guessed, run indented code
        userGuess=input("Sorry, the character(s) you entered is not a correct guess or has already been \nguessed.\nPlease enter a letter ")   #Displaying message to user that input is not correct and to guess again

def wordConvert(letter):   #defining the wordConvert module
    for i in range(len(wordToGuess)):   #repeats the following code which is indented for the number of times the length of the word is
        if wordToGuess[i] == letter:   #if the letter is present in the word to guess the following indented code will be executed
            uncovering[i]=letter   #changes position i to the letter

print("HANGMAN\n\nHello and welcome to hangman! To win this game, all you have to do is to guess\nall of the letters in "
      "the word. Try not to get too many incorrect guesses or\notherwise you will lose.  Good luck!\n")  #prints the welcome and instruction screen

numbGames=0   #set the variable for number of games to have a value of 0
while numbGames<1 or numbGames>3:   #while numbGames is less than 1 or greater than 3
    try:       #try block code is executed
        numbGames=int(input("How many games do you want to play? (Up to 3) "))     #setting numbGames variable to user input
        if numbGames<1 or numbGames>3:     #if numbGames value is less than 1 or greater than 3
            print("Please enter a number which is between 1 and 3 ")   #print message
    except ValueError:    #if error in is present for the try block code the except block will be executed instead.
        print("Please enter a number which is between 1 and 3")    #print message to enter number between 1 and 3

#Main routine
roundNumber=1   #set the roundNumber variable to have a value of 1
while numbGames>0:   #while the numbGames variable has a greater value than 0
    print("Get ready for game", roundNumber, "\n")   #displays the game number to user
    time.sleep(1)   #pauses program for 1 second
    rand=random.randrange(0, len(wordList)-1)   #defining the rand variable by using the random function for a list
    wordToGuess=wordList[rand]   #setting the wordToGuess variable by using the wordList and randomly selecting a word
    uncovering=[]   #creates the uncovering list
    incorrectGuessRem=8   #set the incorrectGuessRem to have a value of 8
    guesses=[]   #creates the guesses list
    for letter in range(len(wordToGuess)):   #for the letter in range for the length of the word the following indented code will be repeated 
        uncovering+=["_"]   #add an underscore to the uncovering list
    while "_" in uncovering and incorrectGuessRem>0:   #while the underscore character is still present in the uncovering list and the value of inCorrectGuessRem is greater than 0
        print("Incorrect guesses remaining:", incorrectGuessRem)   #display incorrect guesses remaining with value from incorrectGuessRem variable value
        for i in uncovering:   #repeats the following indented code for the positon i in the uncovering list
            print(', '.join(str(item) for item in i), end=" ")  #without brackets and quotation marks around each letter position the list of letters is displayed
        print()   #display a space to make GUI more tidier
        print("Letters guessed:", end='')   #display letters guessed with following line next in display
        for i in guesses:   #repeats the following indented code for the positon i in the uncovering list
            print(', '.join(str(item) for item in i), end=" ")  #without brackets and quotation marks around each letter position the list of letters is displayed
        print()   #display a space to make GUI more tidier
        userGuess=input("Please enter a letter ")   #set userGuess variable value to user input
        userGuess=userGuess.lower()   #set userGuess varaible value to lower case
        letterGuess(userGuess)   #use the letterGuess module validate userGuess input
        guesses+=[userGuess]   #add userGuess value to guess list
        if userGuess in wordToGuess:   #if the userGuess value is in the wordToGuess variable execute the following indented code
            wordConvert(userGuess)   #use the wordConvert module to change underscore to correct letter
            print("Yay that letter is in the word!")   #display feedback to user that the letter they guessed is in the word
        else:   #following indented code is executed if userGuess value is not in wordToGuess variable
            incorrectGuessRem-=1   #subtract 1 from incorrectGuessRem variable
            print("Sorry the letter you guessed is not in the word.")   #display feedback to user that the letter they guessed is not in the word
        print()   #display a space to make GUI more tidier
    if incorrectGuessRem==0:   #if incorrctGuessRem value is equal to 0
        print("Sorry but you have run out of guesses! The word you were trying to guess was", wordToGuess)   #display the user has run out of guesses and show what the word was
        print()   #display a space to make GUI more tidier
        roundNumber+=1   #add 1 to roundNumber variable
        numbGames-=1   #subtract 1 from numbGames variable
    else:   #following indented code is executed if userGuess value is not in wordToGuess variable
        print("Congratulations you won!  The word you guessed was", wordToGuess)   #display the user has guessed the word and show what the word they guessed was
        print()   #display a space to make GUI more tidier
        roundNumber+=1  #add 1 to roundNumber variable
        numbGames-=1   #subtract 1 from numbGames variable
