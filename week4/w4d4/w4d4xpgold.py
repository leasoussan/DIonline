# Exercise 1: Temperature Advice
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
import random


get_season=input("Whats' season are we? ")

def get_random_temp(season):

    
    if get_season == "autumn":
        return(random.randint(2,19))
    if get_season == "winter":
        return(random.randint(-10, 1))
    if get_season == "spring":
        return(random.randint(20, 29))
    if get_season == "summer":    
        return(random.randint(30, 45))
    return get_season

print(get_random_temp(get_season))

# Create a function called main().


# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature, together with a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Add more functionality to the main() function, writing some friendly advice relating to the temperature, if it is:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

def main():
    temperature = get_random_temp(get_season) 

    weather =f" The temperature right now is {temperature}"

    if temperature <= 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    if 0 < temperature <= 16:
        print("It's chilli out there")
    if 16 < temperature <= 23:
        print("No neeed coat today, a small jacket will do")
    if 23 < temperature <= 32:
        print(" It's getting hot ")
    if 33 < temperature <= 40:
        print("make sure you get enough water")    

    return weather

print(main())

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, 
# set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. 
# Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’. 
# Make sure to display a meaningful prompt.
# Use the season as an argument when calling get_random_temp().

# Bonus: give the temperature as a floating-point number instead of an integer
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). 
# Determine the season according to the month (this page may help you).)
# 
# 
# 
# 
# Exercise 2: Double Dice
# Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
# Create a function called throw_until_doubles.
# It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
# For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# This function should return the number of times it threw the dice in total. In the example above, it should return 3.

# Create a main function.
# It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you to decide on what data structure to use).

# After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
# Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
# For example:

# If the results of the throws were as follows (your code would do 100 doubles, not just 3):

# (1, 2), (3, 1), (5, 5)
# (3, 3)
# (2, 4), (1, 2), (3, 4), (2, 2)
# Then my output would show something like this:

# Total throws: 8
# Average throws to reach doubles: 2.67.
