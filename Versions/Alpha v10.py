
#HANGMAN ALPHA V9 ANNOTATION V2
#Daniel Hardie

#imports the time and random libraries from the python archives
import random      
import time       

#List of words hard coded in my program
wordList = ["cars", "pear", "jazz", "halo", "flip", "pipes", "pizza", "grape", "banjo", "wheel", "rope", "picture", "shown", "throw", "ticket", "square", "table",
            "chef", "atomic", "galaxy", "sphinx", "oxygen", "chisel", "croquet", "buffalo", "whistle", "numeric", "crafted"]

#defining the chooseRandWord module which randomly selects a word
def chooseRandomWord(wordList):
    i = random.randrange(0, len(wordList)-1)  
    return wordList[i]

#defining the letterGuess module which takes a character input and checks only one letter present and then returns that letter if criteria met as userGuess
def letterGuess(letter):   
    global userGuess
    while len(userGuess)>1 or userGuess not in 'abcdefghijklmnopqrstuvwxyz' or userGuess=='' or userGuess in guesses:
        userGuess=input("Sorry, the character(s) you entered is not a correct guess or has already been \nguessed.\nPlease enter a letter ")  

#defining the wordConvert module which converts the underscore in the game to the correct letter if guessed correctly
def wordConvert(letter):   
    for i in range(len(wordToGuess)):  
        if wordToGuess[i] == letter:   
            uncovering[i]=letter

#displays the welcome and instruction screen
print("HANGMAN\n\nHello and welcome to hangman! To win this game, all you have to do is to guess\nall of the letters in "
      "the word. Try not to get too many incorrect guesses or\notherwise you will lose.  Good luck!\n")  

numbGames=0   #set the variable for number of games to have a value of 0
#this while loop checks that the user input is the number 1, 2 or 3 and asks user to enter input again if not.  This loop determines the number of games to play
while numbGames<1 or numbGames>3:   
    try:       #try block code is executed
        numbGames=int(input("How many games do you want to play? (1 to 3) "))     
        if numbGames<1 or numbGames>3:     
            print("Please enter a number which is between 1 and 3 ")   
    except ValueError:    
        print("Please enter a number which is between 1 and 3")

#Main routine
roundNumber=1   #set the roundNumber variable to have a value of 1
#while there a still more than 0 games to play, show game number, determine word, set the variables to specific values and set lists to empty
while numbGames>0:   
    print("Get ready for game", roundNumber, "\n")   
    time.sleep(1)   #pauses program for 1 second 
    wordToGuess=chooseRandomWord(wordList) #Uses random module to pick a random word from the wordList
    uncovering=[]   
    incorrectGuessRem=8   
    guesses=[]
    #for the letter in range for the length of the word, indented code will be repeated that number of times, setting the underscores for the word
    for letter in range(len(wordToGuess)):   
        uncovering+=["_"]   #add an underscore to the uncovering list
    #while the underscore character is still present in the uncovering list, haven't guessed the word, and the value of incorrectGuessRem is greater than 0, haven't lost
    while "_" in uncovering and incorrectGuessRem>0:   
        print("Incorrect guesses remaining:", incorrectGuessRem)
        #repeats the following indented code for the positon i in the uncovering list
        for i in uncovering:   
            print(', '.join(str(item) for item in i), end=" ")  #without brackets and quotation marks around each letter position, the list of letters is displayed
        print()   
        print("Letters guessed:", end='')
        #repeats the following indented code for the positon i in the uncovering list
        for i in guesses:   
            print(', '.join(str(item) for item in i), end=" ")  #without brackets and quotation marks around each letter position, the list of letters is displayed
        print()   
        userGuess=input("Please enter a letter ")   
        userGuess=userGuess.lower()   
        letterGuess(userGuess)  
        guesses+=[userGuess]
        #if the userGuess value(user input) is in the wordToGuess variable (in the word)
        if userGuess in wordToGuess:  
            wordConvert(userGuess)   #use the wordConvert module to change underscore to correct letter
            print("Yay that letter is in the word!")   
        else:   #incorrect user guess
            incorrectGuessRem-=1   
            print("Sorry the letter you guessed is not in the word.")   
        print()
     #if incorrctGuessRem value is equal to 0 (user lost game)
    if incorrectGuessRem==0:  
        print("Sorry but you have run out of guesses! The word you were trying to guess was", wordToGuess)
        print()  
        roundNumber+=1  
        numbGames-=1   
    else:   #user won game
        print("Congratulations you won!  The word you guessed was", wordToGuess)  
        print()   
        roundNumber+=1  
        numbGames-=1  
