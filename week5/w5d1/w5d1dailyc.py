# Look carefully at this code and output
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


class Farm():
   
    def __init__(self, name):
        self.name = name
        self.animals_dict = {}


    def add_animal(self, animal, quantity=1):
        if animal in self.animals_dict.keys():
            self.animals_dict[animal] += quantity
        else:
            self.animals_dict[animal]= quantity
        print(f"your {animal} was added with {quantity} quantity")
            
        
    def get_info(self):
        print(f"Welcome to {self.name}'s Farm'")
        for animal, quantity in self.animals_dict.items():
            print(f"{animal}:{quantity}")
        print("E-I-E-I-0")   


       

    def get_animal_types(self):
        animal_type = self.animals_dict.keys()
        return(list(animal_type))
     



    def get_short_info(self):
        sentence= f"{self.name} has" 
        animal_type = self.get_animal_types()
        for animal in animal_type:
            if animal == animal_type[0] and ==1 :
                print(f"{sentence} and, {animal}")
            elif animal == len(animal_type)-1:
                print(f"{sentence}, {animal} ")
            else:
                print(f"{animal}.")
        # print(f"{sentence} + {animal_type}")        
# if one animan sentence+= f"{}'

# len(type)-1 last one -2 2 beofre last 

# or
    # def get_short_info(self):
    # sentence = " ,".join(animals[:-1]) "and" + animals[-1]


f1 = Farm("McDonald")

f1.add_animal("cow", 5)
f1.add_animal("sheep")
f1.add_animal("sheep")
f1.add_animal("goat", 12)

f1.get_short_info()


# Create the code that is needed to recreate the code above. 
# Here are a few questions to help give you some direction:
# 1. Create a Farm class. How do we implement that?
# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3. How many method does the Farm class need ?
# 4. Do you notice anything interesting about the way we are calling the add_animal method? 
# What parameters should this function have? How many…?
# 5. Test that your code works and gives the same results as the example above.
# 6. Bonus: line up the text nicely in columns like in the example using string formatting

# Expand The Farm
# Add a method to the Farm class called get_animal_types. 
# It should return a sorted list of all the animal types (names) that the farm has in it. 
# For the example above, the list should be: ['cow', 'goat', 'sheep']
# Add another method to the Farm class called get_short_info. 
# It should return a string like this: “McDonald’s farm has cows, goats and sheep.”
# It should call the get_animal_types function.
# How would we make sure each of the animal names printed has a comma after it 
# aside from the one before last (has an and after) and the last(has a period after)?.



