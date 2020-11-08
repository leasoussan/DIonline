# Daily Challenge : Build Up A String

# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”
# If it’s more than 10 characters, print a message which states “string too long”
# Then, print the first and last characters of the given text
# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
# Example:
# The user enters “Hello Word”
# Then, you have to construct the string character by character
# H
# He
# Hel
# … etc
# Hello World
# Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
# Example:
# Hlrolelwod

import random


sentence = input("Hi give me a a sentence with 10 letters...")

if len(sentence) < 10:
    print("your are missing few letters")
elif len(sentence) == 10:
    print("well Done!!")
else:
    print("WOwo that's way to long...learn to count")


first_char = sentence[0]
last_char = sentence[-1]

print("your first charachter is:", first_char)
print("your last Charachter is:", last_char)    
 
# split_words =""

# for letter in sentence:
#     split_words += letter  
#     print(split_words)

spliting = list(sentence)
random.shuffle(spliting)
mouting_word = ""

for l in spliting:
    mouting_word += l
    print(mouting_word)

