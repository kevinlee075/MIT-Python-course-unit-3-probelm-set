# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0 #initial count is assigned to 0
    for i in secretWord: #check every letter in secretWord
        if i in lettersGuessed: #if a letter in secretWord is also in the list
            count += 1 #add one count and check the next letter in secretWord
        else:
            return False #When any letter in secretWord is not in lettersGuessed, the answer is False
    if count == len(secretWord): #Finally check if counts are equal to the length of secretWord.
    #If yes, it means that the list contains all letters in secretWord and the answer is True
        return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = '' #initially, the answer is an empty string
    for i in secretWord: #Check every letter in secretWord:
        if i in lettersGuessed: #If it's also in the list, copy that letter into the result
            result += i
        else: #If it isn't in the list, add underscore line and a space to the result
            result += '_ '
    return result #return the final answer
        



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = '' #Initially, the answer is an empty string
    import string #Based on the hint, I first import the collection, 'string'
    for i in string.ascii_lowercase: #Check every lowercase
        if i not in lettersGuessed: #If a certain lowercase letter is not in the list,
            result += i #add that letter to the result
    return result #return the fianl answer

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(chooseWord(wordlist))) + ' letters long.')
    n = 8
    for 





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
