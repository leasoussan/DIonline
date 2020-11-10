# Dictionaries 
# # ARE UNORDER so you cant get the first or the last etccc
# # very quick to search inside 
# # Similar to Object in Javascript


# dict{key:value} 
# # the value here is one value 

# set{"value", "value",} 
# # here each of the is a vlaue


# to get a value from a dictionary- it's not order list so you cant get it by an index but using a kew

# list= {
#     "appel": 13,
#     "milk":2,
#     "orange": [1,3,5]
# }
# #  to get the numbers of apples 
# list("apple")

# # you can put as a value another list 
# # Important to know kew ar UNMUTABLE - can be changed
# # a tuple could be a key 


# Define A dictionary
# dog ={
#     "name": "lassy",
#     "age": 3,
#     "breed": "Collie",
#     "Weight": 35,
#     "sex":"male",
#     "alive":True,
#     "food":["Chikcen", "steak", "lamb"]
# }

# print(dog)
# # this will give me steak 
# dog["food"][1]

# dog["price"]= 100
# print(dog)

# # append into Dictionaires
# dog["food"].append("yogurt")
# print(dog)




# -----------------------List of dictionaires--------------------
pets=[
    {
    "name": "lassy",
    "age": 3,
    "breed": "Collie",
    "Weight": 35,
    "sex":"male",
    "alive":True,
    "food":["Chikcen", "steak", "lamb"]
    },

    {
    "name": "Roby",
    "age": 4,
    "breed": "CHaw",
    "Weight": 23,
    "sex":"femal",
    "alive":True,
    "food":["Chikcen", "steak", "lamb"],
    },

    {
    "type": "Ant", "size": 0.01,
    }
]


print(pets)

# to get the size of ants - as we are in a list of dictionaries so we can do the [2]
pets[2]["size"]




# -------Dict of Dict---

# animals ={
#     "pets": {"name": "fluffy", "age": 7}
#     "wild": {"type":"tiger", "size": "very big"}
# }

# # to get the tiger
# animals["wild"]["type"]

# # Always check what is the best data structure to use for my project 


# to change a list into set >>>
# set([list])
# we cant change a list into dictionary the same way 

# when we dont have a value we store a black spot as None 

# if you transfer a dictionary into a list >>>> you get all key names


# dict.key()>>we get a dict.keys >>Another type to get back keys of dictionary >>to make it as list
# nameit = list(dict.key())
# to use it in a loop
# for key in dict.keys


# dict.value()
# dict.items()>> converting this to a list ill get a list of tupple


# list review:

# thing =["a","b","c"]

# thing= list("a", "b", "c")

# thing.append("d")
# thing.insert(position."item")
# things.extend

# ....etc:
    
#     Make DIctionaries
    
# things = {"key": "value"}
# >>to access
# things["key"]
# things["blah"]= "woof" >>>to add
# things["blah"]= "miau">>to change

# things.remove("woof")
# things.update("flah": "chat")

# things["key"]
# thing.get("unexcisitng date")>>>will aloow to request without crashing

# ----------------------------the in Key Word----
# dogs in animals >>>give true or False

# if dog in animal
#     print(f"we have {animals['dog']") >> to get the number of dogs in the dictionary of animals






#     ------------------------loops 

# to get all squared number from 1 to 100 

# numbers = []
# for num in range(1,101):
#     numbers.append(num*num)
# print(numbers)

# >>>> list Comprehension is (builindg a list in one lign)<<<<<<<<<<<<<<<<<<<
# things = []/{}
# things = [values for stuff if condition]>>>>> Depends on what you neeed





# numbers = [num*num for num in range(1,101)]

# numbers = [num*num for num in range(1,11) if num*num % 2 == 0]>> to add here a condition 

# -------------------

# if we want dictionary of numbers and their square -in one ligne 
# 1:1
# 2:4
# 3:9
# etcccc
# numbers = {num:num*num for num in range(1,11)} >>In one ligne 




# _____________________FOR LOOPS _______________________________

basket = {
    "food":["aples","orange", "pears"],
    "clothes" : ["shoes", "socks", "ties"],
    "beers": ["corona","heineken"],
}

# we can loop:

# for key in basket.keys():
#     print(key)

   
# for values in basket.values():
#     print(values) 

# for key, values in basket.items():
#     print(f"The Key is {key} and its value is {values}") 


# You get a tuple list

# ---TO ENUMERAT------


fruits = ["banan", "apple", "orange"]

for item in enumerate(fruits):
    print(item)

if I would like to print strating from number on 
for item in enumerate(fruits):
    print(item[0]+1)

    >>>return to me an object with a list of tupples 


>>> a For loop can have else as well >>.this will give you the else in the last ligne 




    -continue----break--------pass-------


pass is to tell them to do nothing >> can be used while coding and need to loop to pass in order to work on the function 




-----------------------------------WHILE LOOP if __name__ == "__main__":
    basket = []>>an empty element = false 


    while basket:
        print(basket.pop())
    else:
        print("empty")








READ ABOUT 
LIST 
DICTIONARIES 
FOR LOOPS

Comprehension - is one data type can be used with list, set, dictionary 
we have to be carefull bcs that the small list makees it harder to read-put comments 

name = [parameter for perameter in iterable]
ex
my_list = [num for num in range(0,100)]
>> will give me 1 to 100 

>> to get for ex all the numbers multiplay *2 
my_list1 = [num*2 for num in range(0,100)]
>> all will be multipl by 2

>>to get all even item 
my_list3 = [num for num in range(0,100) if num % 2 == 2]
it will give me quicly the list


another ex in a normal way 

some_list = ['a','b','c','b','d','e','d', 'f']

duplicate = []

for value in some_list:
    if some_list.count(value) >1 :
        if value not in duplicate
            duplicate.append(value)
        
print(duplicate)

>>>to make it with the Comprehension


duplicate =[value for value in some_list if some_list.count(value) >1 ]
>>at this point the answer will give me the letters that are double
toavoid having double I put it as a set 

duplicate =list(set([value for value in some_list if some_list.count(value) >1]))

>> we put list because final result should be a list -then it has to go throught a set before that we can get rid of the doubles 



Set Comprehension:
my_list1 = [num*2 for num in range(0,100)]
my_list3 = [num for num in range(0,100) if num % 2 == 2]

>>same as we did before - just take of doubles


simple_dict{
    'a':1,
    'b':2,
}

with dict
my_dict {key:value*2 for key,value in }
>>if we want to creat a Dictionary 