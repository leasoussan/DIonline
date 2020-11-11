# Exercise 1 : What Are You Learning ?
# Write a function called display_message() that prints one sentence telling everyone what you are 
# learning about in this chapter.
# Call the function, and make sure the message displays correctly.

# message= " We are learning to code functions"

# def display_message(subject):
#     return subject


# print(display_message(message))



#  Exercise 2: What’s Your Favorite Book ?
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, making sure to include a book title as an argument in the function call.

# def favorite_book(title):
#     fav_book_sentence = f"My Favorite book is {title}"
#     return fav_book_sentence

# print(favorite_book("Alice in wonderland"))




# Exercise 3 :
# Write a function that accepts one parameter (a number X) and returns the value of X+XX+XXX+XXXX.

# def sum(number):
#     value = number+(number)+
#     return value

# print(sum(2))



# Exercise 4 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

# cities = ["tel-aviv", "afoula", "New-York"]

# def describe_city(city, country="Israel"):
#     temp_list=[]
#     for city in cities:
#         city_location = (f"{city} is in {country}")
#         temp_list.append(city_location)
#     return temp_list

# # print(describe_city(cities ))

# def print_list(list1):
#     for item in list1:
#         print(item)


# print_list(describe_city(cities))


# Exercise 5 : Let’s Create Some Personalized Shirts !
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.

# def make_shirt(size= "Large", text= "I lovePython"):
#     message_to_print = f"This shirt is size{size}, {text}"
  
#     return message_to_print

# make_shirt("M")
# make_shirt("L", "we love everyone" )



# Call the function once using positional arguments to make a shirt.
# print(make_shirt("S", "Cute stuff here " ))    


# # Call the function a second time using keyword arguments.
# print(make_shirt("M", text = "Medium is sexy too " ))    


# # Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# def make_shirt2(size= "Large", text= "I lovePython"):
#     message_to_print = f"This shirt is size{size}, {text}"
#     return message_to_print

# print(make_shirt2())


# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.



# textL_M = "It's good to enjoy life"
# text_O ="You dont need to avoid life so much....enjoy"   
    
# def make_shirt3(size):
#     if size == "L" or "M":
#         message_to_print = f"This shirt is size{size}, {textL_M}"
#     if size != "L" or "M": 
#         message_to_print = f"This shirt is size{size}, {text_O}"
#     return message_to_print

# print(make_shirt3("L"))



# Exercise 6 : Magicians …
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" 
# to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.


# magicians = ["tagada", "oz", "prince", "flower",]
# updated_magicians_list = [] 

# def make_great(magician):
#     # I dont really understand why I had to put this ligne -logic
#     while len(magicians)  != 0:
#         for magician in magicians:
#             adding_title = f"The great {magician}"
            
#             updated_magicians_list.append(adding_title)
#         return updated_magicians_list
    
# print(make_great(magicians))

# print(updated_magicians_list)

# or


# magicians = ["tagada", "oz", "prince", "flower",]

# def make_great(magicians):
#     updated_magicians_list =[]
#     for i in range(len(magicians)):
#         magician = magicians.pop()
#         adding_title = f"The great {magician}"    
#         updated_magicians_list.append(adding_title)
              
#     return updated_magicians_list
    
# print(make_great(magicians))



# Exercise 7: When Will I Retire ?
# The point of the exercise is to check is a person can retire depending on his age and his gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# today_year = 2020
# today_month = 11

# def get_age(year, month):
#     user_year =  today_year - year 
#     user_month = today_month- month  
#     if (user_month > today_month):          
#         today_year = today_year - 1; 
#         today_month = today_month + 12; 
    
#     age=  
    
#     return ()

# print(get_age(1986,7))

# from datetime import date

# def get_age(birthDate):
#     today =date.today()
#     age = today.year - birthDate.year -((today.month,today.day)<(birthDate.month, birthDate.day))

#     return age

# # print(get_age(date(1986,9,7)))


# # After calculating the age of a person, the function should return it (the age is an integer).

# gender= input("What is you gender F/M")
# age = get_age(input("please enter your DOB YYYY/MM/DD"),
    

# def can_retire(gender, date_of_birth):

#     if gender == "F" and age <= int(62):
#         print("Well you are right on time to retire")
#     if gender == "M" and age <= int(67):
#         print("Well Done!!! it's time to tak a break")
#     else:
#         print("you still got some time to go dear")

#     return 

# print(can_retire())

# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age back.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message to the user informing them whether they can retire or not.
# As always, test your code to ensure it works.