# Problem Set 2, hangman.py
# Name: Michael Rodyushkin
# Collaborators:
# Time spent: 2.5 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        check = False
        for char2 in letters_guessed:
            if char == char2:
                check = True
        if check == False:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    final_word = ""
    for char in secret_word:
        check = False
        for char2 in letters_guessed:
            if char == char2:
                check = True
        if check:
            final_word+=char
        else:
            final_word+="_ "
    return final_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    final_word = ""
    for char in string.ascii_lowercase:
        check = True
        for char2 in letters_guessed:
            if char == char2:
                check = False
        if check:
            final_word+=char
    return final_word
def is_already_guessed(letters_guessed, letter):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    letter: String, letter that is being checked if in list
    returs: boolean, True if the letter is a letter guessed; False otherwise
    '''
    for char in letters_guessed:
        if char == letter:
            return True
    return False
def number_of_unique_letters(secret_word):
    unique_letters = 0
    for char in string.ascii_lowercase:
        for char2 in secret_word:
            if char == char2:
                unique_letters+=1
                break
    return unique_letters
def is_in_secret_word(secret_word, letter):
    for char in secret_word:
        if char == letter:
            return True
    return False
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have", warnings_remaining, "warnings left.")
    print("-----------")
    while (not is_word_guessed(secret_word, letters_guessed)) and guesses_remaining > 0:
        print("You have", guesses_remaining, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if str.isalpha(letter):
            letter = str.lower(letter)
            if is_already_guessed(letters_guessed, letter) and warnings_remaining <= 0:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ")
                guesses_remaining-=1
            elif is_already_guessed(letters_guessed, letter):
                warnings_remaining-=1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, " warnings left: ")
            else:
                letters_guessed.append(letter)
                if is_in_secret_word(secret_word, letter):
                    print("Good guess: ")
                else:
                    if letter in "aeiou":
                        guesses_remaining-=2
                    else:
                        guesses_remaining-=1
                    print("Oops! That letter is not in my word: ")
        else: 
            if warnings_remaining <= 0:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: ")
                guesses_remaining-=1
            else:
                warnings_remaining-=1
                print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left: ")
        print(get_guessed_word(secret_word, letters_guessed))
        print("-----------")
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratualiations, you won!")
        print("You total score for this game is:", guesses_remaining * number_of_unique_letters(secret_word))
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for char in other_word:
        letter_in_other = 0
        for char2 in other_word:
            if char == char2:
                letter_in_other+=1
        letter_in_my = 0
        for char3 in my_word:
            if char == char3:
                letter_in_my+=1
            if not char3 in other_word and char3 != "_":
                return False
        if letter_in_my != 0 and letter_in_my != letter_in_other:
            return False
    for i in range(len(my_word)):
        if my_word[i] != other_word[i] and my_word[i] != "_":
            return False
    return True
                


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    list = ""
    for word in wordlist:
        if match_with_gaps(my_word, word):
            list= list + word + " "
    if len(list) == 0:
        print("No matches found")
    else:
        print(list)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have", warnings_remaining, "warnings left.")
    print("-----------")
    while (not is_word_guessed(secret_word, letters_guessed)) and guesses_remaining > 0:
        print("You have", guesses_remaining, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if letter == "*":
                print("Possible word matches are: ")
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                print("-----------")
        else:
            if str.isalpha(letter):
                letter = str.lower(letter)
                if is_already_guessed(letters_guessed, letter) and warnings_remaining <= 0:
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ")
                    guesses_remaining-=1
                elif is_already_guessed(letters_guessed, letter):
                    warnings_remaining-=1
                    print("Oops! You've already guessed that letter. You have", warnings_remaining, " warnings left: ")
                else:
                    letters_guessed.append(letter)
                    if is_in_secret_word(secret_word, letter):
                        print("Good guess: ")
                    else:
                        if letter in "aeiou":
                            guesses_remaining-=2
                        else:
                            guesses_remaining-=1
                        print("Oops! That letter is not in my word: ")
            else:
                if warnings_remaining <= 0:
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: ")
                    guesses_remaining-=1
                else:
                    warnings_remaining-=1
                    print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left: ")
            print(get_guessed_word(secret_word, letters_guessed))
            print("-----------")
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratualiations, you won!")
        print("You total score for this game is:", guesses_remaining * number_of_unique_letters(secret_word))
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    #To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
