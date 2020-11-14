# Exercise 1
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.
# Exercise 2
# Using the list sandwich_orders from Exercise 1, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
# Exercise 3
# Draw the following pattern using for loops:

#   *
#  ***
# *****
# Draw the following pattern using for loops:

#     *
#    **
#   ***
#  ****
# *****
# Draw the following pattern using for loops:

#     *
#     **
#     ***
#     ****
#     *****
#     *****
#      ****
#       ***
#        **
#         *
# Exercise 4
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
# my_list = [2, 24, 12, 354, 233]
# for i in range(len(my_list) - 1):
#     minimum = i
#     for j in range( i + 1, len(my_list)):
#         if(my_list[j] < my_list[minimum]):
#             minimum = j
#             if(minimum != i):
#                 my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# print(my_list)
