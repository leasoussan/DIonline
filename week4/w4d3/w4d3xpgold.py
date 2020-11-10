# Exercise 1: Birthday Look-Up
# Create a variable called birthdays. Its value should be a dictionary.

birthday = {
    "leo": "2000/02/10",
    "lara": "2010/01/11",
    "lena": "1990/01/09",
    "sonia":" 1999/01/08",
    "bob": "1986/06/03"
}


# name = input(f"Hi  , what name are you looking for")
# print(f"His birthday is {birthday[name]}")


# Initialize this variable with birthdays of 5 people of your choice. 
# For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. 
# Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message to the user. Then tell him: “You can look up the birthday of the people in the list!”“
# Ask the user to give you a person’s name and store his answer in a variable.
# Get the birthday for the person’s name from the birthdays dictionary.
# Print out the birthday with a nicely-formatted message.







# Exercise 2: Birthdays Advanced
# Before asking the user to type in a person’s name, print out all of the names from the dictionary, to make it easier for them to choose.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have birthday information for “”)


# name = [print(name) for name in birthday.keys()]>>not good 

# for name in birthday.keys():
#     print(name)

# name_request = input("Please chose a name")


# try: 
#     print(f"The birthday is {birthday[name_request]} dont forget to tell him :)")
# except:
#     print(f"Sorry we don't have birthday information for {name_request}")



# Exercise 3: Add Your Own Birthday
# Insert this new code: before you offer the user to type a person’s name to look up, ask the user to add a birthday first:
# Ask the user for a person’s name – store it in a variable
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# The rest of your code should follow (from Exercise 2).
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

# username = input("what your name?")
# userdob = input("What the Birthday")
# birthday[username] =userdob

# name_request = input("Please chose a name")


# try: 
#     print(f"The birthday is {birthday[name_request]} dont forget to tell him :)")
# except:
#     print(f"Sorry we don't have birthday information for {name_request}")

# print(birthday)




#  Exercise 4: Fruit Shop:
# Create a new dictionary called items and add the following key-value pairs to it using code. They each represent an item and its price
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# Print all the items and their prices in your dictionary in a human-readable way

# fruits= {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# for fruit, price in fruits.items():
#     print(f" {fruit} is {price}")

# for fruit, price in fruits.items():
#     stock = int(input(f"how many {fruit} do you have"))
#     fruits[fruit] = {"price": price,
#                     "quantity": stock}



# print(f"the total price would be: {sum([priceQuantity['price'] * priceQuantity['quantity'] for priceQuantity in fruits.values()])}")



# Add stock information to each item (keep track of how many of each item our shop has).
# Once you’ve added stock info to the item, write some code to figure out how much it would cost to buy your entire stock of all items





# Exercise 5 : Cars
# Copy the following string into your script: “Volkswagen, Toyota, Ford Motor, Honda, Chevrolet”
# Convert it into a list using Python (don’t do it by hand!).
#
cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet, kia"

cars_list =cars.split(", ")
# print(cars_list)


# print(len(cars_list))
#  Print out a message saying how many manufacturers/companies are in the list.

# Print the list of manufacturers in reverse/descending order (Z-A).
# reversed_list =sorted(cars_list, reverse=True)
# print(reversed_list)

# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# print([car for car in cars_list if "o" in [char for char in car]])
# # 

# other option 
# import re
# print([car for car in cars_list if re.match("\w*[Oo]+\w*", car)])
# here i tell hikm if inside a word \w* ...+\w*, car regex tells me to put the item im checking from which is car here as the begining of the lign


# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

cars_noI =[]

for car in cars_list:
    if "i" not in car:
        cars_noI.append(car)
print(len(cars_noI))


# Print out the above information with meaningful output messages.


# Bonus: There are a few duplicates in this list [“Honda”,”Volkswagen”, “Toyota”, “Ford Motor”, “Honda”, “Chevrolet”, “Toyota”]:
# Remove these programmatically. (Hint: you can use sets to help you).
lists_cars = ['Honda','Volkswagen', 'Toyota', 'Ford Motor', 'Honda', 'Chevrolet', 'Toyota']
car_update = set(lists_cars)
cars_str = " ".join(car_update)

# print(f"There are {len(car_update)} cars Brands; which are: {cars_str}")

# Print out the companies without duplicates, in a comma-separated list with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), and also print out a message saying how many companies are now in the list.
# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

for car in car_update:
    car_reversed 
    car ==sorted(car, reverse=True)
print(car)

