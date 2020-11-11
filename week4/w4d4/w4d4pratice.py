# def say_hello():
#     """A function that says hello"""
#     print("Hello!") 

# # say_hello()
# -------------------------

# # to calculat numbers 
# def add(num1,num2):
#     return num1+num2

# def add(num1,num2):
#     answer= num1+num2
#     return answer


# to calculate exponant
# def power(base, exp):
#     answer = 1
#     for i in range(1,exp+1)
#         return answer
# --------------------------------------

# if my function doesnt have parameter I can't givi it to here - 
# when a function have a paramater to work it will wait for an argument to be able to befired


# -----------VARIABLE SCOOP ------------------------------
#  if it's defined inside a function we can get it only inside a function 
# if variable is declared outside a function you can git it inside the function and outside

# whu will we use a fonction: to be able to put them in logical blocs and more readble 
# simplifying talking about code like ordering humberguer and not asking for bread and meet and other topping
# to avoid repeating yourselffor ex

# def send_email(to_address,name, message, subject, from_address)
# .....   

# if sign_up ==True:
#     send_email("lea@go.com, "dana", "thank you forsigning up", "you just signed up", "from@our.com")

# positional argument = are the order of your argument. as it could mess up the answers or results 


# ------------------------key word argument----------------------------------------------------------------
# def say_hello(username, language):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     else:
#         print("This language is not supported: " + language)

# say_hello("lea", "EN")

# # writing the lign above the order matters, but with positional arguments like here it doesnt matters 
# say_hello(username="lea", language="EN")


# def say_hello(username, language="EN"):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     else:
#         print("This language is not supported: " + language)

# say_hello("Rick")
# # OR
# say_hello(username="Rick")

# DEFAULT VALUE == is when we like in the finction here def say_hello(username, language="EN"):
# we have a default value,meanng that their arguments are optional.
# in the ex above the language is optional as it's a default value
# first you have to put your positional orgument then your default



# say_hello("Rick", "FR")
# # OR
# say_hello(username="Rick", language="FR")

# # ----------------RANGE----------------------------
# # a range is basically a stop at the end of the range
#  def range(stop)

# def range(start, stop)
 
#  def range(start, stop, step =1)
# #  first you have to put your positional orgument then your default
# #  so you cant have 

#  def range(start=0, stop, step )

# no to mix with list[start:stop:step]
# --------------------------SORTED_--------------------
# 
# sorted(arr)>>creat an new list with a version of the list sorted 


# arr.sort() = sort the actual array - when it's done it does nothing and return NONE





# -----------Returning a value-------------------------
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician)



# def blah():
#     a=1
#     b=2
#     c=3
#     print(a, b, c)
# >>> you get back a tupple


# PRINT_______Are not inside a function - we need to do return then call it



# --------max(arr)------------to get the biggest num
# --------min(arr)------------to get the smallest num
# --------sum(arr)------------to get the total num



# ----------CLASSE PRACTICE-------------------
# write a function that has 1 parameter called mylst
# must retur total sum of the list 

account =[2345, 234, 456, -2345]



def sum(my_list):
    total = 0
    # we start of 0 this is the position of the first number 
    for num in my_list:
        total += num
    
    return total 
        


print(sum(account))



---------------MinList--------------
def min_list(my_list):
    

def max_list(my_list):






# -----EX---- Exercise
# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

# For example:

# def calculation(a, b):
#     # Your Code

# res = calculation(40, 10)
# print(res)



# ___________________FUNCTION 2___________________
# 1. Passing List As Function Arguments

# def greet_users(users):             # users should be a list
#     for user in users:              # Because it's a list, we can loop through it
#         print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

# usernames = ["steve", "stan", "debbie"]
# greet_users(usernames)




# 2.Seeing Functions As Address





# 3. Modifying A List In A Function
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
# completed_models = []

# Simulate printing each design, until none are left. 
#  Move each design to completed_models after printing. 
# while len(unprinted_designs) != 0:    
#     current_design = unprinted_designs.pop() 

#     # Simulate creating a 3D print from the design.    
#     print("Printing model: " + current_design)    
#     completed_models.append(current_design)    

# Display all completed models. 
# print("\nThe following models have been printed:") 
# for completed_model in completed_models:    
#     print(completed_model)