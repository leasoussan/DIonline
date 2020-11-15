# classe are producting elements - 
# ex of str type is a class, every time i use str() i can access all methode to it li str.upper() str.lower() etccc

# class have Capital letter as naming VS. function
# smalle_letter() == function/methode 
# Big_letter/Bigletter= class 

# ex 
# class Str:
#     def lower():
#         pass
#     def upper():
#         pass 
#     etcc

# INSTANTIATION = the creation of an object instance of the class - we make class doll the INSTANTIATION will be creating a doll call "dolly"

# in the process of the insantiation you have to give it a "soul" you give me self to be able to distinguish it self
# ex bank account:
# each bank account will have to have his own functionalities etc.

# we will creat his own behaviour

# class BankAccount():

#     def __init__(self, account_number balance=0 ):
#     # init is for initialization of the object with self and the others parameter we want- the below are attributes
#         self.account_number= account_numberthis is reference to the parameter)
#         self.variable = variable
#         self.transaction =[]

#         here we can add anything we would like to have in the object 


# # to be able to get the variable everywhere we have to defin them with self.

    
#     def view_balance(self):
#         # self.transaction.append("view Balance")// we append the title to print
#         print(f"Balance for account"{self.account_number: {self.balance}")
    
#     def deposit(self, amount):
#         if amount <= 0 
#             print("Invalid amount")
#         elif amount < 100:    
#             print("Min amount to desposit is 100")
#         # return none // we return none that its exiting the function when amount is -withdraw and not deposit
#         else:
#             self.balance += amount
#             self.transaction.append("Desposit {amount}")
#             print(f"deposit of {self.balance} successfuly done")

#     def view_transaction(self):
#         print("transaction")
#         print("-------------")
#         for transaction in self.transaction:
#             print(transaction)

#     def withdraw(self,amount):
#         if amount > self.amount:
#             print("notenought money here")
#         else:
#             self.balance -= amount
#             self.view_transaction.append(f"Withdrwa: {amount}")
#             print("approved withdrar")
#             return amount


# >>>>> to get info 
# my_account = BankAccount("111", "1222")
# my_account.deposit(100)
# # we add into deposit 
# my_account.view_balance()
# # check the deposit 

# -------------------------other object----------------

# class Student():

#     def __init__(self, name):
#         self.name = name

#     def sayHi(self):
#         print(f"Hi my name is {self.name}")


# class School():

#     def __init__(self, name):
#         self.name = name
#         self.students =[]

# # to get students anme here we are accessing a list so list[0] ex


#     def enroll(self, student):
#         self.students.append(student)



# Exercise
# Analyse this code. What will be the ouput ?

# Explain the goal of the __init__() method

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# >>init + initialization of the class point - main parameters 
# ## create an instance of the class
# p = Point(3,4) 

# ## access the attributes
# print("p.x is:", p.x) >>  "p.x is 3"
# print("p.y is:", p.y) >> "p.y is 4"


# ------------------------
# Exercise
# Analyse this code. What will be the output ?

# Explain the goal of the methods

# Create a method that modifies the name of the person

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello my name is " + self.name)
# add a function to change the name
    
    def change_name(self, new_name):
        self.name = new_name

# p1 = Person("John", 36)
# p1.myfunc()
# 

//tip for calling function - action keep as verb if bool>> as a question





#  Exercise
# Analyse this code. What will be the output ?





# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# computer1 = Computer()
# computer1.brand = "Apple"
# print(computer1.brand)

# computer2 = Computer()

# Computer.description(computer2, "Mark")
# # IS THE SAME AS:
# computer2.description("Mark")