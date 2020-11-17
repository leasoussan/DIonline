# Exercise 1 : Built-In Functions
# Python has many built-in functions, and if you do not know how to use it, you can read document online.
# But Python has a built-in document function for every built-in functions.

# Write a program to print some Python built-in functions documents, such as abs(), int(), raw_input().
# And add documentation for your own function

# def absolut(num):
#     '''
#     Return the absolut number for a Number 

#     Calling the function with int/float
#     Returns: number or integer with absolut value 

#     '''

#     return -num if num < 0 else num    
#     print("")
# print(absolut(-1234520.20))





# Exercise 2: Currencies
# Recreate these results
# Hint : When you add 2 currencies, if they don’t have the same label raise an error
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)
# >>> str(c1)
# '5 dollars'
# >>> int(c1)
# 5
# >>> repr(c1)
# '5 dollars'
# >>> c1 + 5
# 10
# >>> c1 + c2
# 15
# >>> c1 
# 5 dollars
# >>> c1 += 5
# >>> c1
# 10 dollars
# >>> c1 += c2
# >>> c1
# 20 dollars
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

# class Currency:
#     def __init__(self, currency, amount):
#         self.amount = amount
#         self. currency = currency

#     def __int__(self):
#         return self.amount

#     def __str__(self):
#         if self.amount > 1:        
#             return str(self.amount)+" "+ self.currency+"s"
#         return str(self.amount)+" "+ self.currency

#     def __repr__(self):
#         return f"{self. amount} {self.currency}s" if self.amount >1 else f"{self. amount} {self.currency}"
        
    
#     def __add__(self, other_currency):
#         total = self.amount
#         if self.currency == other_currency.currency:
#             total += other_currency.amount
#             return total    
#         else:
#             raise ValueError("you need to change your currency first ")


# c1 = Currency('dollar', 12)
# c2 = Currency('dollar', 10)
# c4 = Currency('shekel', 1)
# c3 = Currency('shekel', 10)

# Look at the lesson on Datetime Module for the exercises 3,4,5

# datetime module
# import datetime
# from datetime import date
# from datetime import time




# def to_Januray():

#     to_date = datetime.datetime(year = 2021, month = 1, day = 1)
#     today = datetime.datetime.now()

#     count_down = to_date - today
#     print("January First is in ", count_down)




# print(to_Januray())   




# Exercise 3:
# 1.Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st January is in 10 days and 10:34:01hours)






# Exercise 4:
# Write a function that display today’s date, the amount of time left from now until the next holiday, 
# additionally print what holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours)
# Hint: Start with hardcoding the datetime and name of the holiday

# Exercise 5 : How Old Are You In Jupiter ?
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you were told someone were 1,000,000,000 seconds old, you should be able to say that they’re 31.69 Earth-years old.


# Exercise 6 : Faker Module
# Install the faker module, and read the documentation.
# Create an empty list called users. Tip: It’s a list of dictionaries
# Create a function that adds dictionaries to the users list. Each user has the properties: name, adress, langage_spoken. 
# Use faker to populate them with fake data.

# users= {}
# name 
# address
# language langage_spoken


from faker import Faker


fake= Faker()
# for name in range(20):
#     print(fake.name(), fake.address(), fake.language_name())


def populat_user(amount):
    users_list ={}

    for user in range(0,amount):
        users_list[user]= {}
        users_list[user]["name"]= fake.name()
        users_list[user]["address"] = fake.address()
        users_list[user]["language"] = fake.language_name()
    print(users_list)

populat_user(20)        

# print(type(populat_user))

