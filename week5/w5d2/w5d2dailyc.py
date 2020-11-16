# Dailly Challenge Tips

# to check inheritance is to to is A 
# is a 
# inheritanc ex dog is an animal

# has a 
# composition 
# car has an enging 
# >>is a class with another class inside


# Daily Challenge : DNA
# This challenge is about Biology.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.

# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, 
# meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosome, and it can also mutate the same way Chromosomes can.
# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and a environement parameter that 
# sets the probability for its DNA to mutate.
# Instantiate a number of Organims and let them mutate until one gets to a DNA is only made of 1s. 
# Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion

import random


class Gene():
    
    def __init__(self, value):
        value = random.randint(0,1)
        self.value = value



print(gene1.value)

# class Chromosome():
#     def __init__(self, gene):
#         self.gene = Gene() 

    # def mutate(self):        
    # mutate = randint(.5)
    #     pass

#         return int(Gene()) * 10

         


# class Dna():
#     def __init__(self, chromosome):




# class Organims():
#     def __init__(self, dna, environement):
#         self.dna = dna
#         self.environement = environement

    
