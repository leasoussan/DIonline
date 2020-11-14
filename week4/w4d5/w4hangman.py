# Use python to create a Hangman game.

# The Rules:
# The computer choose a random word and mark out blanks (short lines) for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer write the letter in everywhere it would appear.
# If the letter isn’t in the word then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.

# Starter Code
# Here is a piece of code that will give you a random word, just put it above your program and work from this.
import random
import re

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 



# gallow =
# """___
# |   O
# |  /|\ 
# |   |
# |  /|\
# _|_
# """

# here we want to get a random word and to put it hiden (with stars) for the lenght of the word
    #
def get_word():
    word = random.choice(wordslist) 
    chosen_word = list(word)
    return chosen_word


print("Hello Welcome to the Hangman ....Let's Play!")

# def guess_letter():
#     while True:
        
#             continue   
#         else:
#             print("this is not a letter")
#         return input


def is_validate(guess):
    if guess.isalpha():
        return True
    return False


# # 
def play():
    # word = get_word()
    word="check"
    print(word)    
    word_index = list(enumerate(word, 0))
    print(word_index)
    complet_word = list("*" * len(word))
    wrong_guessed_letters=[]
    tries= 6
    guessed = False

    print(complet_word)
    

   
    # we give a false condition in the begining that we could after change it in the ocnditional to True
    while tries > 0:
        guess_letter = input("please guess a letter ")
        # check if letter is valid and the lenght 
        if len(guess_letter) > 1 and guess_letter != is_validate:
            print("please put only one letter and check your input")
        else:

            if guess_letter in wrong_guessed_letters:
                print("you already guessed this one")
                
                
            elif guess_letter not in word:
                print("Wrong letter try again ")
                tries -= 1
                wrong_guessed_letters.append(guess_letter)
                print(f"wrong guess {wrong_guessed_letters}")
                print(f"you've got more {tries} tries")
        

           
            else:
                #  guess_letter in word_index:
                # index = word.index(guess_letter)
                # print(index)
                # complet_word[index] = guess_letter
                # # if we have few letters to replace: 
                indeces = [index for index, letter in word_index if letter == guess_letter]
                print(f"indeced results{indeces}")
                for index in indeces:
                    complet_word[index] = guess_letter
                print(complet_word)
        
       
            if len(complet_word)== len(word):
                if complet_word == word:
                    guessed = True
                    print("Well done") 

                else:
                    print("nice try but it's not this ")

print(play())



# steps

#first get a random word
# then start function play set up conditions and list to append elements 
# we would ask for input check that it's a letter and that there is one letter by letter- if ok continue
# the we check if letter in the word we chose 
# if its not in -print no in and take of count 
# if in get the letter by number and change it
# outer level- if the new word holder (check with lengh) is = 0 then check if the wordcomplete = word 
# if equal the word the print 
# else no the word and finish 




