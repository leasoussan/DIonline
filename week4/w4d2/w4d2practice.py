# we comments only when we thing someone might need to understand hwat we did and not why we did it

# data storage:
# primitive (simple - iteger, string, sloat and boolean)
# and non primitive (lists Array(sequances), files, Tuples, sets and DIctionaries)

# immutable- can't be changed
# mutable- can be changed
# some stuff in Python are Immutable

# # Example
# letters =["a", "b", "c"]
# # array is a list in Python
# to change one of the letter 
# letter[2]=zwill change the c into z
# lists are mutable
# we cantchange strings -they are immutable- to be able to change it you have to reassigne them to make the mutable 
# sequence is not a data type is a string

# text = [start:stop:step]
# where to start- where to end and skip in that range every x step
# if for ex you dont know what the end you can do [1::2] leaving blank
# or if you want to start from the begining [:5]from 0 to 5 
# [:] count everything


# topring revers order 
# number =[1,2,3,4,5,6,7,8,9,10]
# number[::-1]
#     print(number)

# # list can be storing anythong we want 
# to address into a list list[2] - using index to give  a valut 
# list[2]= "new word"


# list object has few methods
# append() add new item at END of list 
# list.append("banana")>>to add bananas at end of list- every time well get an item from user we ll apend 
# if we want to add a specifique position

# remove("soemting")= will search by the word
# pop() to specifie the Index of what we want to remove ex list.pop(3)remove the 3rd item
# you can a make a varibale new =list.pop(3) will store the item into a variable- it returns you the item that was removed
# pop()empty one will pop the last one


# you can add 2 listes:
# list1=[""]
# list 2=[""]
# groceries = list1 +list 2

# or extend list.extend["item", "item"]

# len(groceries)>>.will give the lenght of our list 

# number=[1,2,3,]
# sum(numbers)>>.will give the sum of the numbers ---can mix words and number


# sorting sequences
# numbers=[3,4,2,5,3,5]
# sorted(number)
# sorted(letters)---forletters 
# !! it will not change the variable but give us a copy of the sorted array.
# if you wold like to keep it numbers2 = sorted(numbers)

# or numbers.sort() belog to the string- 

# sorted() and sum() doesnt change the original variable but gives you a copy.

# insert() to inster at particulat position 
# list.insert(2,"item") at position 2 insert this item 



ex Practice:
list=[4,6,9,32,45,32,45,78,]

list.index(45)
the first occurance of an item (45)we ll get the position
so to change something in the list 
fount_item = list.index(45)
list(fount_item)=200 will change the number45 to 200



nested lists
matrix = [
    [1,2,3,],
    [4,5,6],
    [7,8,9]
]


matrix = [
    [1,2,3,], [4,5,6],[7,8,9]]

    to get number 6 
    >> matrix[1][2]
    >>to get number 8 
    >> martix [2][1]

-----------
tuple =() and set={} (lesssed used that list and dictionaries)

set >>unorder list {}
set1 = {"a", "b", "c"}
checking type(set1)
they are unorde so no set1[0] >>wont work

if a set have a double - set will remove it for you - for ex sorting out emails or usersname etccc
to convert list to set 
>> set(list)

set will allow to get specific stuffs -methods
union()
intersection()



TUPPLE - UNMUTABLE list 
cant be changed

tupl =("a", "b", "c") round ()
you can use index tupl[2]

but you cant change it!!! to protect data and uncahnge it- for ex days of a week are i a TUPLE 
if you sort a tuple >>you get back a list as it doesnt change the original tuple-
for ex if you have set data in a game hen you want it to change you ll get a converted value into an array- then the tuppple will be still referance when game start again
 


 ___________LOOPS

 for loops 
shopping = ["apples", "bred", "chocoloat"]
for item in shopping:
    print(f"im buying{item}")

I will get for every item the sentence with the item 


for <entry> in <list>
You can loop throug a set a tuple 

counting in a loop-----------------

If I want to loop through a biger number i loop through a range 
range (100) only for numbers

for i in range(10):
    print(i)

for i in range(start, end,steps)
    print(i)
    >> will give us 

for i in range(100, 200,10)
    print(i)
    >> 100, 110, 120 ....till 200 

-----chr(3) >>this will give from a number to a letter 
-----ord(a) will give us the nummber of this letter 

range object >>>> is also a type 
to generate numbers when yo uneed them - and not all of them - as much as you can 

for i in list(range(100, 200,10))
    print(i)
    >> 100, 110, 120 ....till 200 
>> adding list before will make it a list

 while loops 
not so usefull

if <condition>:
    run this 
else:
    run this

the condition has to be true - meaning you are comparing a true to the reste 
you need to break in order to go out of a loop 
continue will be to continue the function after checking for a condition 

example
users = ["adam", "bob", "charlie", "admin"]
for person in users
    if person =="admin":
        continue
    print("Hello", person)


    >>this will give us hello to all the people except admin


--------------to run until condition
cart = []

while True:
    item = input("what do you want ")
    if items.lower() =="stop":
        break

    this will stop as sson as we enter the sord stop

    cart.append(item)
    # to add tot he cart
# out of the list 
print("your chart contane:\n")
for item in chart
print(item)

this iwll print in a new line :\n the chart 

if we want to add numbers - show the index number 
>>print(chart.index(item)+1, item)
>>>>we add 1 that it doesnt start at 0

- if we want to be a, b c 
print(chr(chart.index(item)+65), item)
>>65 being a 

to be bale to get the number of the items
print(f"you have {len(chart)} items"})
when we use format this allows us to enter methods 