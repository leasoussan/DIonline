# Exercise 1: Formula
# Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# We will take a comma-separated string of numbers from the user, then, use each number from the user as D in the formula and return all the results
# For example, let’s assume the following comma separated input sequence is given to the program: 100,150,180
# The output of the program should be:

# 18,22,24

# from math import sqrt

# C = 50 
# H = 30 



# answers= []
# number = input("give me a csv (comas separated variable number)").split(",")
# # there is no int before as it's a string so we ll convert them after to number 
# for number in numbers 
#     q=sqrt((2*C*int(number))/H)
#     answers.append()

# or answers.append(str(round(sqrt((2*C*(number))/H))))
# # instead of one ligne 
# print(answers)
#  to round numbers to no decimal we add round() arround the whol equation and how many decimal- default is 0 decimal 
#  we add str before to get the ansers in str that we ll be able to put it into a list 



# Exercise 2 : List Of Integers
# We are given a list of 10 integers to analyze. Repeat the questions below with the following lists of numbers:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# Store the list of numbers in a variable.
# We will now print some information about the list of numbers. Each time, print the answer together with a helpful message that tells the user what you are printing.

# Print the following information:
# a. The list of numbers – printed in a single line
# b. The list of numbers – sorted in descending order (largest to smallest)
# c. The sum of all the numbers

# A list containing the first and the last numbers only.
# A list of all the numbers greater than 50.
# A list of all the numbers smaller than 10.
# A list of all of the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# The numbers without any duplicates – also print how many numbers are in the new list.
# The average of all the numbers.
# The largest number.
# 10.The smallest number.
# 11.Bonus: Find the sum, the average the largest and smallest number without using builtin functions.
# 12.Extra bonus: instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100.
# a. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each answer from the user should be added onto a list variable that you created earlier.
# b. After asking the user 10 times, you should now have a list of integers.
# c. Print a line to separate the input section (getting the numbers from the user) from the output section).
# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it into your code, and store it as a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…)
# How many sentences it contains
# How many words it contains
# How many unique words it contains
# Bonus: How many non-whitespace characters it contains
# Bonus: The average amount of words per sentence in the paragraph
# Bonus: the amount of non-unique words in the paragraph
# Exercise 4
# Write a program to compute the frequency of the words from the input.
# Tip: The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1



#  Exercise 5 : Information From The User
# Take the following inputs 5 times from the user:
# Name (string)
# Age (int)
# Score (int)
# Build a list of tuples using these inputs, each tuple will contain a name, age and score
# Sort the list by the following priority Name > Age > Score
# If the following tuples are given as input to the script:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]



# EXTRA QUESTION

# ask a user for a radius of circle and calculate the radiu of a area from it 

radius = float(input("give me a number to calculate the radius"))
pi = (3.14159/4) 
area = pi * (radius * radius)

print(f"the area is {area}")
s