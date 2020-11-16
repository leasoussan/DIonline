# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle
# print(nc.color)



class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)


nc = NewCircle(1)
print(nc.diameter)
nc.grow()
print(nc.diameter)

---------------Class Practice--------------------
import random 
import py print


class Animal():
    def __init__(self, name, age, weight):
        self.name = name
        self.name = age
        self.weight = weight

    def play(self):
        print("Im happy !")
    
    def have_bithday(self):
        self.age += 1

    def eat(self):
        self.weight +=1


class Dog(Animal):
#   no need here for init as it's an extention of the animal class- inheriting basic and have his own character
# the __init__function runs from animal 
    def play(self):
        print("whoofff  barked, WAF !")

    def play(self):
        print("Im happy dog !")
# here we can extend from dog to others dogs 

class PoliceDog(Dog):

    def controling(self):
        print("whatch out")

    # if i will call the play function for the police dog, and there is no play here it will first cehck the play at DOG then in ANimal 

    def play(self):
        pass
# putting pass will cancel the def

    def eat(self):
        self.weight += 3 

        # to overwirte a methode 


class Cat(Animal):

    def play(self):
        print("miao")

    def play(self):
        super().play()
        # the super will send us to the parent function - child class can access parent parents cant access child 

--------------------------------

#
class Dragon():
    def __init__(self,name, age, weight, treasure):
        super().__init__(name, age,weight)
        self.treasure = treasure

    # if I want to add something in the init i have to give the super INIT then add self 
    # 
       


1    when you creat an instance,that class init function willcallit automaticaly 
2   if a methode cant be findin a class python will look in the parents



-----------------
Modules 

import as- to give a new namen
numpy is numerical usage > import numpy as np (shortre version)
import pprint >>to get dictionaories printed better


__________-you can import another py file and call is 
ex import w5d2dailyc to get (w5d2dailyc.py) (which is in the same folder)
or from w5d2dailyc import * 

_ goo to have one py file to wrtie the code and another one to write the code

seperate declaration and implementation


------------------EXCEPTION----------------------ffrom exceptional 
def play(url):
    # to get to play videos  
    pass 
cat_video = "http://youtube...."
play(cat_video)
>>> what if the video is not hereanymore? 

>>>python gives soltion: 
try run this code:
    here
if it fails:
    run this 


    ---------------

try: 
    num = int(input("enter a number"))
    num_square = num * num
    print(num_square)
except ValueError as e:
    print("something when wrong") 
    num = int(input("enter a number"))
    num_square = num * num
    print(num_square)
    
except ValueError as e:
    print(e)
    # will give a smaller message- built in function

except InsufficientFund:

    print("you dont have ..a...")
except XYZ:
    print("")
    login again 
    or other actions 


to avoid the system to crash!! it will try onething if goes wrong>>>print   



raise ValueError("you are not allowed")>>> this is to creat your own error 
for ex if someone doesnt have the right age - its not a computer problem its ValueError
we dont want to the computer to crash so we raise an error

try:

    age = int(input("How old are you?"))

    if age < 18:
        raise ValueError("you are not old enough")

    print("welcome")

except:


    ------------
def findMax(myList):
    if not isinstance(myList, list):
        raise TypeError("Please use the  list")

    big = myList[0]
    for num in myList:
        if num > myList:
            big =num
    return big

    to give messages 