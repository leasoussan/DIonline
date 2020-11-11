# Daily Challenge : Solve The Matrix
# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, 
# select only the alphanumeric characters and connect them, then he replaces every group of symbols 
# between two alphanumeric characters by a space.

# Using his technique, try to decode this matrix:
import string 

alphabet_upper = string.ascii_uppercase
alphabet_lower = string.ascii_lowercase

def neoRead (*args):
    sentence = ""
    for element in args:
        # loop one to get number of colum 

        element.split("")
        # indexing element and build up row 
        for letter in element:
            if letter == alphabet_upper or alphabet_upper:
                sentence +=letter
            if letter is not alphabet_upper or alphabet_lower:
                letter.pop()    
    return sentence



print(neoRead("7 3", "Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"))

# logic check 
# 1- I would like to split the elements to be able to read through
# 2- I have an empty lst to append all good letters 
# 3- I would like to read the charachters and check if thery are letters
# 4- I would like to remove what ever is not a letter 
#    





    #    element.__len__()> 0:
 