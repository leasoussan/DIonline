# Exercise 1 – Random Sentence Generator
# Description: We will create a program that will generate a random sentence and display it to the user.
#  We will allow the user to choose how long the sentence will be.

# Hint : The random sentences do not need to make sense or to be grammatically correct

# Download this word list

# Save it in your development directory.
# response = requests.get("http://norvig.com/ngrams/sowpods.txt")

# Create a function called get_words_from_file that will read the file’s contents and return them as a collection. What data type should you use?
import random


# def get_words_from_file():
   
#     with open('sowpods.txt', 'r')as f:
#         data = f.readlines()
            
#         return list(map(lambda x: x.replace('\n',''), data))

# # print(get_words_from_file())



# def get_random_sentence(number):

#     words = []
    
#     for i in range(number):
#         word =random.choice(get_words_from_file())
#         words.append(word)
#     sentence = ','.join(words)
#     return sentence.title()
#     # make sure join expressions are not in the loops

# # print(get_random_sentence(4))


# def main():
#     """
#     Main function will request the user to enter amount of words 
#     Return a gibrish sentence :) 

#     """
#     number= int(input("how many words would you like to get in your sentence? between 2 and 20"))

#     if number <= 2 or number >= 20: 
#         raise ValueError("need to be between 2 and 20 please")
#     print(f'your sentence is {get_random_sentence(number)}') 


# main()


# class SentenceGenerator():
    

#     def __init__(self, number):
#         number = input("chose a number ")
#         if number <= 2 or number >= 20:
#             raise ValueError("Input has to be between 2 and 20")
#         else:     
#             self.number = number

#     # @staticmethod
#     def get_words_from_file(self):
#         with open('sowpods.txt')as f:
#             data = f.readlines()
#             return list(map(lambda x: x.replace('\n',''), data))

       

#     def get_random_sentence(self):
#         word = [random.choice(data) for _ in range(self.number)]    
 
#         sentence =",".join(words)

            
                    


# Create another function called get_random_sentence. 
# It should have a single parameter, length, which will be used to determine how many words the sentence should have. 
# The function should get the words list, and choose random words from it, according to the amount specified by length.

# The words should be joined together into a string, which should be formatted in lower case (or title case) and returned.

# Create a main function. It should:

# Print a message explaining what the program does.

# Ask the user how long the sentence should be. Acceptable values: an integer between 2 and 20. Validate your data, and test your validation!

# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, user your functions to create a random sentence, and then display it proudly to the user.




# Exercise 2: Working With JSON
import json


sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
# Access the nested key “salary” from the above JSON-string
# Sort the dictionary key-value pairs inside “payable” alphabetically, by their key, using code
# Save the dictionary as JSON to a file

# 
data= json.loads(sampleJson)
payable =data["company"]["employee"]["payable"]
# salary =data["company"]["employee"]["payable"]["salary"]
# print(salary)
data_dict_items=list(payable.items())
print(data_dict_items)

payable_sorted =sorted(data_dict_items, key=lambda t: t[0])
print(payable_sorted)

payable_dict= dict(payable_sorted)
print(payable_dict)

data["company"]["employee"]["payable"] =payable_dict
print(data)


json_data= json.dumps(data)

with open('w5d4.json', 'w')as f:
    f.write(json_data)
