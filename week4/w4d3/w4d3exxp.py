# Exercise 1 : Convert Lists Into Dictionaries
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# numbers = zip(keys,values)
# print(tuple(numbers))




# Exercise 2 : Cinemax #2
# “Continuation of Exercise Cinemax of Week4Day2 XP”

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Here is the object you will work with : family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Using a for loop, the dictionary above, and the instructions, print out how much each family member will need to pay alongside their name
# After the loop print out the family’s total cost for the movies
# Bonus: let the user input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty)
#
# # name_age = input("Please give me your name and age(seperated by coma")
# family = {}

# while True:
#     for guest in name_age:  
#         family= guest
#     print(family)

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# for key, value in family.items():
#     print(f"{key} has to pay {value}")

# total = sum(list(family.values()))
# print(f"your Total today is : {total}")

# ------------------Teacher Correction--------------------
# name_age = input("Please give me your name and age(seperated by coma")

# for name, age in family.items()
# if age <3:
#     price = 0
# if age >=3 and age <=12:
#     prince = 10
# if ages >12 :
#     price =15 

# print(f"{name} pays {price}")


# Exercise 3: Zara
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: France -> blue, Spain -> red, US -> pink, green 
# Create a dictionary called brand, and translate the information above into keys and values.
# #  
# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"], 
#     "number_stores": 7000, 
#     "major_color": {"France":"blue", "Spain":"red", "US": ["pink", "green"]}
#     }

# #Change the number of stores to 2.

# brand["number_stores"] = 2


# # Print a sentence that explains who the clients of Zara are.

# type = (f"{brand['name']} clients are:{brand['type_of_clothes']}")
# print(type)

# # Add a key called country_creation with a value of Spain to brand

# brand["country_creation"] = "Spain"

# # If the key international_competitors is in the dictionary, add the store Desigual.

# brand["international_competitors"].append("disengual") 

# # Delete the information about the date of creation.

# brand.pop("creation_date")

# # Print the last international competitor.

# print(f"One of our Competitors is {brand['international_competitors'][-1]}")




# # Print in a sentence, the major clothes’ colors in the US.

# # print(f"The major clothes clolors in the us are: {brand['major_color']['us']}")

# #  print(brand)


# # Print the amount of key value pairs (length of the dictionary).
# print(f"Brand had {len(brand)} elements inside")

# # Print only the keys of the dictionary.
# print(f"Brand keys are {list(brand)}")

# # Create another dictionary called more_on_zara with the following information:
# # creation_date: 1975 
# # number_stores: 10 000 
# more_on_zara ={
#     "creation_date": 1975,
#     "number_stores": 10000
# }

# brand.update(more_on_zara)

# print(brand)
# # Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# # Print the value of the key number_stores. What just happened ?
# print(f"Number Stores {brand['number_stores']}, woow What just happennnedddd???")
# # 
# 
# 
#  Exercise 4 : Disney Characters
# Consider this list :

users = [ "Mickey", "Minnie", "Donald", "Ariel", "Pluto"] 

indices = list(range(len(users)))


disney_users_A =dict(zip(users,indices))
disney_users_B = dict(zip(indices,users))
disney_users_C = dict(zip(sorted(users), indices))

# print(disney_users_A)
# print(disney_users_B)
# print(disney_users_C)

disney_users_D = {key: value for (key, value) in disney_users_A if "i" in key}
disney_users_E = {key: value for (key,value) in disney_users_A.items() if key.startswith("M") or key.startswith("P")}
print(disney_users_E)
print(my_list)
 
# #1/ print(disney_users_A) >> {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}


# #2/ print(disney_users_B) >> {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ print(disney_users_C) >> {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# Use a for loop to recreate the #1 result. Tip : don’t hardcode the numbers
# Use a for loop to recreate the #2 result. Tip : don’t hardcode the numbers
# Use a method to recreate the #3 result
# Hint: The 3rd result is in the alphabetical order
# Recreate the #1 result, only if:
# The characters’ names contain the letter “i”.
# The characters’ names start with the letter “m” or “p”.

