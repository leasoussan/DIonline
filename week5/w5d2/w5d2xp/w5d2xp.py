# # Exercise 1 : Pets
# # Consider this code

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def walk(self):
#         return f'{self.name} is just walking around'


#     def __repr__(self):
#         return self.name
#         # to get the name in representing


# class Bengal(Cat):
#     def sing(self, sounds):

#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Persian(Cat):
#     def speak(self, sounds):
#         return f'{sounds}'





# # # 
# # # Add another cat breed
# # # Create a list of all of the pets (create 3 cat instances from the above) 
# # my_cats = []
# # # Instantiate the Pet class with all your cats. Use the variable my_pets
# # # Output all of the cats walking using the my_pets instance

# # cat1 = Bengal("Jojo",12)
# # cat2 = Chartreux("Liri",6)
# # cat3 = Persian("loan",3)

# my_cats = [Bengal("Jojo",12), Chartreux("Liri",6), Persian("loan",3)]
#     # they inherit form Cat - creat 3 object from 3 a subclass of the class cat  


# my_pets = Pets(my_cats)
# my_pets.walk()


# # 
# 
# 
# 
# Exercise 2 : Dogs
# Create a class named Dog with the attributes name, age, weight
# Implement the following methods for the class:
# bark: returns a string of “ barks”.
# run_speed: returns the dogs running speed (weight/age *10).
# fight : gets parameter of other_dog, 
# returns string of which dog won the fight between them, 
# whichever has a higher run_speedweight* should win.




class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print("Barks")    
    
    def run_speed(self):
        return ((self.weight/self.age) * 10 )

    def fight(self, other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed()* other_dog.weight):
            return f"{self.name} won the battle"
        return f"{other_dog.name} wont the battle"

d1 = Dog("Jojo", 12, 12)
d2 = Dog("Riri", 9, 16)
d3 =Dog("Fifi", 4, 2)



# Create 3 dogs and use some of your methods

# TRY WITH CALL 

# class Dog():
#     def __call__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         print("Barks")    
    
#     def run_speed(self):
#         return ((self.weight/self.age) * 10 )

#     def fight(self, other_dog):
#         other_dog = Dog()
#         if (self.run_speed * self.weight) > other_dog:
#             return f"{self.name} won the battle"
#         return f"{other_dog.name} wont the battle"









