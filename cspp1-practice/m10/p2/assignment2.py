'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    global list_a
    list_a = list("abcdefghijklmnopqrstuvwxyz")
    for i in letters_guessed:
        if i in list_a:
            list_a.remove(i)
    return ''.join(list_a)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    flag = True
    if letters_guessed not in secret_word:
            flag = False
    return flag

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    lists1 = []
    for i in secret_word:
        if i not in letters_guessed:
            lists1.append("_")
        else:
            lists1.append(i)
    return ''.join(lists1)

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

def hangman(secretWord):
    le=len(secretWord)
    print("Secret word has",le,"words")
    i=0
    num_guesses=8
    letters_guessed=[]
    global x
    while(num_guesses>=1):
        print("you have",num_guesses,"guesses left")
        print("please guess a letter")
        letters_guess=input()
        print("availble letters ")
        print(get_available_letters(letters_guess))
        if (letters_guess in secretWord):
            if (letters_guess in letters_guessed):
                print("already given that word")
                x=get_guessed_word(secretWord,letters_guessed)
            else:
                letters_guessed.append(letters_guess)
                print(letters_guessed)
                print("good guess")
                x = get_guessed_word(secretWord,letters_guessed)
                print("Available letters")
                print(get_available_letters(letters_guessed))
        else:
            x=get_guessed_word(secretWord,letters_guessed)
            print("oops!! that letter is not in my word")
            num_guesses-=1 
        if(str(x) == secretWord):
            print("Congratulations you won")
            break
        if(num_guesses==0):
            print("sorry you ran out of guesses My word was",secretWord)
    
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
    # FILL IN YOUR CODE HERE...



def main():  
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    #secretWord = chooseWord(wordlist).lower()
    #hangman(secretWord)
    secretWord = "hello"
    hangman(secretWord)


if __name__ == "__main__":
    main()
