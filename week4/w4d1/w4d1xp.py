# EX 1: print 5 time Hello World 


# number = 0

# while number < 5:
#     print("Hello World")
#     number = number + 1

# # or

# say_hello = "Hello World"

# for number in range(5):
#     print(say_hello)





# -------------------------------# EX 2
# Calculate the result of: (99^3) * 8

# base =99
# exponenet =3
# multiplicator =8 
    
# result = (base**exponenet)* multiplicator
# print (result)

# # or 

# result2 = pow(base, exponenet)*8
# print(result2)




# -----------------EX3
# Predict the output of the following code snippets:

# >>> 5 < 3  false


# >>> 3 == 3 true
# >>> 3 == "3" false
# >>> "3" > 3 false (e\its error)
# >>> "Hello" == "hello" false


# EX4_-------------------------

# Exercise 4 : Your Computer Brand
# Create a variable called computer_brand that contains the brand of your computer.
# Insert and print the above variable in a sentence,like "I have a razer computer".

# computer_brand = "Lenovo"

# print(f"I have a {computer_brand} Computer")




# Exercise 5: Your Information
# Create a variable called name, and give it your name as a value (text)
# Create a variable called age, and give it your age as a value (number)
# Create a variable called shoe_size, and give it your shoe size as a value
# Create a variable called info. Its value should be an interesting sentence about yourself, including your name, age, and shoe size. Use the variables you created earlier.
# Have your code print the info message.
# Run your code

# name = "lea"
# age = 34
# shoe_size = 39

# info = f"Hello my name is {name}, and I'm {age}, i like to run with my shoes size {shoe_size}"

# print(info)





# Exercise 6: Odd Or Even
# Write a script that asks the user for a number and determines whether this number is odd or even.

# age = int(input("hi what is you age"))
# if age%2 == 0:
#     print("even")
# else:
#     print("odd")



# Exercise 7 : What’s Your Name ?
# Write a script that asks the user for his name and determines whether or not you have the same name, print out a funny message based on the outcome

# my_name = "lea"
# user_name = input("What is your name?")

# if user_name == my_name:
#     print("lol we have the same name")
# else:
#     print("cool name!")



# Exercise 8 : Tall Enough To Ride A Roller Coaster
# Write a script that will ask the user for their height in inches, print a message if they can ride a roller coaster or not based on if they are taller than 145cm
# Please note that the input is in inches and you’re calculating vs cm, you’ll need to convert your data accordingly

# your_height = float(input("what's your hight in inches?"))

# hight = your_height * float(2.54)
# min_height = 145

# if hight >= 145:
#     print("Well Done you are height enough to roll!!!")
# else:
#     print("Go get some more soop")