# Exercise 1 : Geometry
# Write a class called Circle that receives a radius as argument (default is 1.0)
# Write two instance methods to compute perimeter and area
# Write a method that prints the geometrical definition of a circle
# from math import pi

# class Circle():
#     def __init__(self, radius):
#         self.radius = radius

#     def get_perimeter(self):
#         perimeter = 2* pi * self.radius    
#         return perimeter


#     def get_area(self):
#         # area= (self.radius * self.radius) * pi
#         area= pow(self.radius, 2) * pi
#         return area

#     def geometrical_def(self):
#         print(f" {self.get_area()} {}")






# Exercise 2 : Custom List Class
# Write a cit rustom list class called MyList, eceives a non empty python list 
# (check that it is actually a list in your code!!)
# Write a method that returns reversed list
# Write a method that returns sorted list
# Write a method that generates a list of the same length containing random numbers (use list comprehension)



class MyList():

    def __init__(self, my_list):
        # if isinstance(my_list, list): len(my_list) > 0 :
        #     self.list = my_list
        # else:
        #     print("your list is empty, please upload other")
        if type(my_list)== list:
            if len(my_list)>0:
                self.list = my_list
                print("thank you for uploading")
            else:
                print("please upload a list")    

    def reversed(self):
        # reversed_list = self.list.reverse() 
        return self.list[::-1]
        # we can't use reversed function here as it's retrunes in place 

    def sorted(self):
        sorted_list = sorted(self.list)
        return sorted_list


# list1= MyList(["hello", "how", "are", "you"])
# list2= MyList([])



# Exercise 3 : Restaurant Menu Manager
# The purpose of this exercise is to create a menu of a restaurant. 
# As a Manager we will be able to add and delete dishes.

# Create a python file called menu_manager.py

# Create a class called MenuManager.

# Create a method __init__ that instantiates an attribute called menu. 
# This variable is a list of dictionaries that contains dishes. 
# Each dish has a name, a price, a spice level and a gluten index (this key is a boolean).
# Below, are the dishes currently offered to the customers.

# Soup – 10 – B - False
# Hamburger – 15 - A - True
# Salad – 18 - A - False
# French Fries – 5 - C - False
# Beef bourguignon– 25 - B - True
# Meaning: For the spice level:
#    • A = not spicy,
#    • B = a little spicy,
#    • C = very spicy
# Translate this information into the menu attribute.

# Create a method called add_item(name, price, spice, gluten). 
# This method adds the new dish in the menu.

# Create a method called update_item(name, price, spice, gluten). 
# It checks if the dish is in the menu, if it is, then update it. If it isn’t, send a message to the manager

# Create a method called remove_item(name). 
# It has to check if the dish is in the menu, if it is, then delete it and print the dictionary. 
# If it isn’t, send a message to the manager.

