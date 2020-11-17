# Daily Challenge : Information From The User
# Notice : solve this using a lambda function, even if you can think of another way
# Hint: Look at the lesson on Week4Day4

# Take the following inputs 5 times from the user:
# Name (string)
# Age (int)
# Score (int)
# Build a list of tuples using these inputs, each tuple will contain a name, age and score
# Sort the list by the following priority Name > Age > Score
# If the following tuples are given as input to the script:


usrs_info= [tuple([input("Please enter your name,age and score separated by coma")]) for user in range(5)]
usrs_info.sort(key=lambda t: t[0])

print(usrs_info)

# # how this works 
# mylist = [3,6,3,2,4,8,23]
# sorted(mylist, key=WhatToSortBy)



# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


