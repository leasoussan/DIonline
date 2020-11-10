# Exercise 1 : Favorite Numbers
# Create a set called my_fav_numbers with your favorites numbers.
# Add two new numbers to it.
# Remove the last one.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

# my_fav_number= [7, 8,6, 18, 26]
# my_fav_number.append(33)
# my_fav_number.append(70)
# print(my_fav_number)

# my_fav_number.pop()
# print(my_fav_number)


# my_fav_number= [7, 8,6, 18, 26]
# friend_fav_numbers =[50,70]
# our_fav_numbers = my_fav_number + friend_fav_numbers
# print("our lucky numbers are", our_fav_numbers)



# Exercise 2: Tuple
# # Given a tuple with integers is it possible to add more integers to the tuple?
# tuple1 = (4,3,4,5,)
# NO



# Exercise 3: Print A Range Of Numbers
# Use a for loop to print the numbers from 1 to 20, inclusive.

# for num in range (21):
#     print(num)


# Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way of generating a sequence of floats?
# Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.
# import numpy

# for num in numpy.arange(0, 11, 0.5):
#     print(num)






# Exercise 5: Shopping List
# Consider this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Put “Kiwi” at the end of the list.
# Add “Apples” at the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# basket.pop(0)
# basket.pop()
# print(basket)

# basket.append("kiwi")
# print(basket)

# basket.insert(0, "Apples") 

# print(basket)

# count = basket.count("Apples")
# print(count)
# # question ow to use her capitalize()

# basket.clear()


# print("your basket is emty", basket)



# Exercise 6 : Loop
# Write a while loop that will keep asking the user for input until the input is the same as your name.

# name = "lolita"

# while True:
#     guessing = input("Guess a name with letters L A I A T lower case")

#     if guessing != name:
#         print("Nice try but NOO")
#         continue
#     else:
#         print("BRAVO")
#         break



# Exercise 7
# Given a list, use a while loop to print out every element which has an even index.

# names= ["jean", "george", "lola", "david", "chiko", "chika", "chikititita", "mahlouf"]

# while len(names):
#     if names.index % 2 == 0: 
#         printindex(names)
    
# # or
# even_names = names[::2] 
# print(even_names)


# 
#  Exercise 8
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

# for three in range (3, 31, 3):
#     print(three)




# Exercise 9
# Use a for loop to find numbers between 1500 and 2700, which are divisible by 7 and multiples of 5.

# for num in range(1500, 2700):
#     if num%5 ==0 and num%7 ==0 :
#     print(num)


# Exercise 10: Favorite Fruits
# Ask the user to type in his/her favorite fruit(s) (one or several fruits).
# Hint : Use the input built in method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list. (How can we ‘convert’ a string of words into a list of words?).
# Now that we have a list of fruits, ask the user to type in the name of any fruit.
# If the user’s input is a fruit name existing in the list above, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT a fruit name existing in the list above, print, “You chose a new fruit. I hope you enjoy it too!”.
# Bonus: Display the list in a user friendly way : add the word “and” before the last fruit in the list – but only if there are more than 1 favorites!


# fev_fruit= input("what are your favorits fruits, please seperate with coma")

# prefered_fruits= fev_fruit.split()


# for fruit in range(5):
#     type_fruit = input("give me a fruits")

#     if type_fruit != fev_fruit:
#         prefered_fruits.extend(type_fruit)
#         print("nice this is a new one...Bonn'Apetit i added to the list")    
       
#     else:
#         print("Yes you told me this...give mesome others")
    
    
# print(f"so you like{fev_fruit}")



# Exercise 11: Who Ordered A Pizza ?
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exit print all the toppings on the pizza and what the total is (10 + 2.5 for each topping)

# topping =[]
# total = 10
# while True:
#     enter_topping =input("Enter your topping, press quit to end your request")
#     if enter_topping.lower() == "quite":
#         break
#     topping.append(enter_topping)
# for i in range(len(topping)):
#     i = 0.25
#     total += i
    
# print(f"your toping are:\n{topping}, and your total is {total}")
    




# Exercise 12: Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Apply it to a family, ask the user what the age of each of the people that want a ticket is.
# Store the total cost of all the tickets for this group and print it out.
# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which one can see the movie.
# Tip: Try to add the allowed ones to a list.

# y=True
# n = False
# ticket_price = []
# nb_people = []

# age = int(input("how old are you guy?"))
    
# for i in range(age):
#     nb_people.append(age)
#     add =input("add person? y/n")
#     if add != n:
#         continue       
#     else :
#         print(f"your ages are{nb_people}")
#     break

# for i in tickets:
# if pers < 3:
#     ticket == 0
# elif 3 < pers <12 :
#     ticket == 10
# else:
#     ticket ==15




# Exercise 13 : Who Is Under 16?
# This time you have a list of users, and you want to remove every user that is below 16 years old.

# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# At the end, print the final list.



# users = ["David","ori", "shira", "loli", "lola"]


# for user in users:
#     age = int(input(f"hi {user} how old are you"))
#     if age > 16:
#         continue 
#     else:
#         users.remove(user)
#         continue

# print(users)

# correction 
# this is a problem to remove someone as it might skip indexes 

# users = ["David","ori", "shira", "loli", "lola"]
# users_16 =[]

# for user in users:
#     age = int(input(f"hi {user} how old are you"))
#     if age >= 16:
#         users_16.append(user)
# print(users_16)

# or
# for i in range(len(users)):
#     age = int(input(f"hi {user} how old are you"))
#     if age <16:
#         users.remove(user)
#         i -= 1
        # the second sulution is better as creatin a second list is more database so we are better with removing the right  
        # the problem of index is set when we do decementing the list 

# Exercise 14: Family Members
# Using a while loop keep asking a user for input, these inputs will be used to control a menu
# On the menu we will have 4 options:
# Add a name
# If the user selects this ask for the name to add
# Remove an existing name
# If the user selects this ask for the name to remove
# View family members
# Print a nice list of the family members names
# Exit

guest_list = []
add_name = ("What name would you like to add")
remove_name = ("What name shoud I remove")


while True:
    question = "What would you let to do? :\n add guest type add. :\n to remove a guest type remove :\n to print your guest list print guests"
    print(question)
    break