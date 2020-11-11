# Exercise 1 : What’s Your Name ?
# Write a function called get_full_name() that receives three arguments: a first_name, a middle_name and a last_name.
# But the middle_name should be optional, if it’s omitted by the user, 
# the name returned will only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

def get_full_name(first_name, last_name, *args):
    name = f"{first_name} + {args} + {last_name}"
    return name

print(get_full_name(first_name="lea", middle_name="nada", last_name="soussan")) 



# Exercise 2 : Box Of Stars
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, 
# one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************
# 
# def box_printer (*args):
#     for word in args:
         
#         print(":\n word")
        
            
# # 
# # 
# 
# 
# 
# 
# 
# Exercise 3
# Analyse this code before executing it. Write some comments next to each line and find the output.
# What is the purpose of it ?
# def insertion_sort(alist):
#    for index in range(1,len(alist)):
# # the index will start at 1 and not 0 up the lenght of the list - so number 54 is not in the array
#     currentvalue = alist[index] 
# # the current value will be the first number of the index for the lenght of 8 item (one is off)   
    
#     position = index
#     # position is the position of the int in the index
    
#     while position>0 and alist[position-1]>currentvalue:
#         # as long as the index is bigger than 0 AND the value of the item before is bigger than the current value 
#         # the position in the index of this element (numb) will move one position down because it's a bigger number 
#         # and the index will shift as well  
#         alist[position]=alist[position-1]
#         position = position-1
# # the position of alist index is equal the currentvalue 
#     alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)




# Exercise 4 : From English To Morse
# Write a function that converts English text to Morse code and another one that does the opposite.
# Hint: Check on internet for translation table, every letter is separated with a space and every 
# word is separated with a slash /.