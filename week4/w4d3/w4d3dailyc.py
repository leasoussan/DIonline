# Daily Challenge: Caesar Cypher
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques. 
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number 
# of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 
# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher, 
# the user entries the program, and then the program asks him if he wants to encrypt or decrypt, 
# and then execute encryption/decryption on a given message and a given shift.

# More information on caesar cipher is available on internet.

import string, random

text = "cats are cool"

cyper_text=[]
 for letter in text:
     cyper_text += chr(ord(letter)+3)



# # question to be dealing with 
# how do you deal with space 
# what do you do when arriving to z


# ti shift +3 we can do 
chr(ord(letter) +3)


alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)
getting_letter = alphabet_list*4

# print(getting_letter)
desordered_list = [letter for letter in getting_letter[5::random] ]



print(desordered_list))
# decryot_alpha = zip(alphabet_list, desordered_list)

# decrypt = dict(decryot_alpha)

# print(decrypt)

# message = input("Hi welcome to our code language, what would you like Encrypt (enter E) or Decrypt (enter D)")


# if message == D:
#     for letter 