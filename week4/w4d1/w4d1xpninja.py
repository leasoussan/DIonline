# Exercise 3 : Outputs
# Predict the output of the following code snippets:
#     >>> 3 <= 3 < 9  true
#     >>> 3 == 3 == 3 true
#     >>> bool(0) false
#     >>> bool(5 == "5") fasle
#     >>> bool(4 == 4) == bool("4" == "4") False
#     >>> bool(bool(None)) False
#     x = (1 == True) true
#     y = (1 == False) false
#     a = True + 4 >5
#     b = False + 10 > 10

#     print("x is", x) >>x is true 
#     print("y is", y) >> y is false
#     print("a:", a)5
#     print("b:", b)10




# Exercise 4 : How Many Characters In A Sentence ?

# Use python to find out how many characters are in this text using a single line of code (beyond the establishment of your text variable).

# import textwrap

# my_text= """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
#            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#            Ut enim ad minim veniam, quis nostrud exercitation ullamco 
#            laboris nisi ut aliquip ex ea commodo consequat. 
#            Duis aute irure dolor in reprehenderit in voluptate velit 
#            esse cillum dolore eu fugiat nulla pariatur. 
#            Excepteur sint occaecat cupidatat non proident, 
#            sunt in culpa qui officia deserunt mollit anim id est laborum."""

# print(len(my_text))




# Exercise 5: Longest Word Without A Specific Character

# 1. Keep asking the user to input the longest sentence they can without the character “A” in it
# 2. Each time a user successfully sets the new longest sentence print a congratulations message



while True:
    noA_sentence = input("Write a sentence without the letter a in it")
    if "a" in noA_sentence:
        print("please  try again ")
        continue
    else:
        print("Well DONNNEEEEEE!")
        break

    # check why the loop is not stoping