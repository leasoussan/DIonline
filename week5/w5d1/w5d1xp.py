# //rememeber :
# 1.wathc your syntax
# 2. objects (coockies) vs Classes (coockie cutter)

# Exercise 1: Cats
# Consider this class

# class Cat:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# # Instantiate 3 Cat objects using our class
# # Create a function that finds the oldest cat and returns the cat
# # Print out: “The oldest cat is , and is years old.” using the method previously created
    

# cat1 = Cat("loli", 10)
# cat2 = Cat("lola", 14)
# cat3 = Cat("lolu", 5)

# def oldestCat(*cats):
#     max_age = 0
#     oldestCatName = ""
#     for cat in cats:
#         if cat.age > max_age:
#             max_age = cat.age 
#             oldestCatName = cat.name
#     print(f"The oldest cat is: {oldestCatName} is {max_age}")


# other solution

# def find_oldest(cat_list):
#     oldest_cat = cat_list[0]
#     for cat in cat_list:
#         if cat.age > oldest_cat.age
#         oldest= cat 
#     return oldest_cat
# oldest cat = find_oldest[cat1,cat2,cat3]


# list_of_cats= [Cat(chr(65+i),randInt(1,10) for i in range(10))]
# to creat a random list of 10 cats







# Exercise 2 : Dogs
# # Create a class Dog.
# class Dog():

#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#         print(f"Hi im{self.name} and i am{self.height} cm")
# # In this class, create a method __init__, that takes two parameters : nameand height. 
# # This function instantiates two attributes, which values are the parameters.
# # Create a method named bark that prints “ goes woof!”

#     def bark(self):
#         print(f"{self.name} goes Woof")

# # dog1.bark()>>print name goes woof


# # Create a method jump that prints the following “ jumps cm high!” where x is the height*2.
#     def jump(self):
#         jump_hight = self.height *2
#         print(f"{self.name} can jump {jump_hight} cm")


# dog1 =Dog("a", 10)


# # Outside of the class, create an object davids_dog. 
# # His dog’s name is “Rex” and his height is 50cm.
# # Print the details of his dog by calling the methods.
# davids_dog = Dog("Rex", 50)


# # Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# # Print the details of her dog by calling the methods.
# # Create an if statement outside of the class to check which dog is bigger. 
# # Print the name of the bigger dog.
# sarahs_dog = Dog("Teacuo", 20)

# dogsList= [dog1, davids_dog,sarahs_dog]



# def bigger_dog(dogsList):

#     biger_dog = dogsList[0]

#     for dog in dogsList:
#         if dog.height > biger_dog.height:
#             biger_dog = dog
#     return biger_dog.name   



# Exercise 3 : Who’s The Song Producer ?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics(a list).
# Inside your class create a method called sing_me_a_song that prints each 
# element of lyrics on his own line.
# Create an object, for example:
# # Then, call the method sing_me_a_song. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven




# class Song():

#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)



# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()












# Exercise 4 : Afternoon At The Zoo
# Create a class Zoo
# In this class create a method __init__ that takes one parameter: zoo_name
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method add_animal that takes one parameter new_animal. 

import string 


class Zoo():
   
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals =[]


    def add_animal(self, new_animal): 
        if new_animal in self.animals:
            print("already here")
        else:
            self.animals.append(new_animal)
            return self.animals


# This method adds the new_animal to the animals list, only if the new_animal isn’t already in the list.
# Create a method get_animals that prints all the of animals in the zoo.

    def get_animals(self):
        for animal in self.animals:
            print(f"{animal}")

# Create a method sell_animal that takes one parameter animal_sold. 
# This method removes the animal from the list, only if he was already in the list.


    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"no such animals for sell we dont have {animal_sold}")

# Create a method sort_animals that sorts the animals alphabetically and groups 
# them together based on their first letter.


    def sort_animals(self):
        animals_sorted_alpha ={}
        numbers={}
        for leters in range(chr(65, 90)):

            if self.animals.items[chr[0]] == self.self.animals.items[chr[0]]:
                listed_alpha.number= animal
                print(listed_alpha)
    # firt sorting the animals
    animals = sorted(animals) #we put in a variable that we get a new list 
    # 
    sorted_animals={}
    key =1 
    starting_letter = animal[0][0] #A

    for animal in animals:
        # checing first the starting letter
        if animal[0] != starting_letter
            key += 1
        # ow if there is nothing at this key 
        if key not in sorted_animals:
            sorted_animals[key] = animal
        # if it's in sorted animals and there is a key already 
        else:
            if not isinstance(sorted_animals[key], list)
                sorted_animals[key].append(animal)
            sorted_animals[key] = [sorted_animals[key]]
            # here to say if there is already a key dont make a new key. but add the animal else just add it 
           

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
#
#  Create a method get_groups that prints the animal/animals inside each group.
# Create an object ramat_gan_safari and call all the methods.
# Tip: for each method, the argument should be the answer of the zoo keeper.
# Example

# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)





z1=Zoo("teva")

z1.add_animal("cat")
z1.add_animal("lion")
z1.add_animal("cow")
z1.add_animal("birds")
z1.add_animal("Ape")
z1.add_animal("Baboon")
z1.add_animal("cougar")
z1.add_animal("bear")
z1.add_animal("emu")
   

# new_animal = Zoo.add_animal(input("animal name"))


