

# # Exercise 1
# # Write a script that inserts an item at a defined index in a list.
# list = ["place1", "place2", "place3", "place4"]

# list.insert(3,"added aimed between 3 and 4 ")
# print(list)







# # Exercise 2
# # Write a script that counts the number of spaces in a string.

# # space = 0
# sentence = "homm many  pace is ther is here on here o oa"
# counting= sentence.count(' ')
# print(counting)
# # or

# #  for i in sentence:
# #     if (i.isspace()):
# #         space = space+1
# # print(space) 







# # Exercise 3
# # Write a script that calculates the number of upper case letters and lower case letters in a string.

# story= "This Day was crasy and I didnt want to Go"
# count = len([word for word in story if word.isupper()])
# print(count)







# Exercise 4
# Write a function to find the max of a list


# list = [89,1,3,50]

# def findMax(list):
#     max_num = list[0]
#     for number in list:
#         if number> max_num :
#             max_num = number
#         return max_num

# print(findMax(list))






# # Exercise 5
# # Write a function that return factorial of a number

# #     >>>Factorial(4)
# #     >>>24
# number =4
# factorial =1
# for i in range(1 ,number+ 1):
#     factorial =  factorial*i
# print(f"The factorial of {number} is {factorial}")











# Exercise 6
# Write a function to find the sum of an array without using the built in function:

#     >>>MySum([1,5,4,2])
#     >>>12

# list=1,5,4,2
# def sum(numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#     return sum 
# print(sum(list))    












# Exercise 7
# Write a function that counts an element in a list (without using the count method):

#     >>>list_count(['a','a','t','o'],'a')
#     >>>2
# list_to_count= (['a','a','t','o'],'a')

# def count_element(list):
#     list_lenght =
#     for i in list:
#         if i == type(list):
#             i = 1
#         list_lenght += i 
#     return list_lenght   

# print(count_element(list_to_count))







# Exercise 8
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

#     >>>Norm([1,2,2])
#     >>>3
# ​









# Exercise 9
# Write a function to find if an array is monotonic (sorted either ascending of descending)

# num1 = [7,6,5,5,2,0]
# num2 = [2,3,3,3]
# num2 = [1,2,0,4]


# def isMonotonic(numbers):
    
#     return (all(numbers[i] <= numbers[i + 1] for i in range(len(numbers -1)) or 
#             all(numbers[i] >= numbers[i + 1] for i in range(len(numbers -1)))
    
# print(isMonotonic(numbers))


#     >>>isMono([7,6,5,5,2,0])
#     >>>True
# ​
#     >>>isMono([2,3,3,3])
#     >>>True
# ​
#     >>>isMono([1,2,0,4])
#     >>>False





 
# Exercise 10
# Write a function that prints the longest word in a list.
# sentence = ["hollywood", "cestnimportque", "is", "good"]
    
# def long_word(text):
#     word_lenght = 0
#     for word in text:
#         if len(word) > word_lenght:
#             word_lenght = len(word)           
#             longuest_word= word
            
#     return longuest_word

# print(long_word(sentence))            





# Exercise 11
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
# list_toSort = ["banana", 1, "yellow", 12, 23, "Summer"]


# def sortingList(list):
#     for item in list_toSort:
#         numbers= [item for item in list_toSort if isinstance(item, int)]
#         words= [item for item in list_toSort if isinstance(item, str)]

#         return numbers, words 


# print(sortingList(list_toSort))








# Exercise 12
# Write a function to check if a string is a palindrome:

#     >>>isPalindrome('radar')
#     >>>True
# ​
#     >>>isPalindrome('John)
#     >>>False
# 
# 
# 






# Exercise 13
# Write a function that returns the amount of words in a sentence with length > k:
# sentence = "all right lets beguine a ou i lol let see"

# def check_words(text, k):
#     textCheckWord= text.split()
    
#     total= sum(1 for word in textCheckWord if len(word) >= k)

#     return total

# print(check_words(sentence, 3))        
  










# # Exercise 14
# # Write a function that returns the average value in a dictionary (assume the values are numeric):
    
# info= {'a': 1,'b':2,'c':8,'d': 1}

# # >>>DicAvg({'a': 1,'b':2,'c':8,'d': 1})
# # 
    
# def get_average(checkAvg):
#     data =sum(checkAvg.values()) 
#     divider= len(checkAvg.values())
#     average = data / divider
#     return average

# print(get_average(info))












# Exercise 15
# Write a function that returns common divisors of 2 numbers:

#     >>>CommonDiv(10,20)
#     >>>[2,5,10]
# def communDiviser(numInpt):
    # numbers = [num for num in numInpt if  ]





# Exercise 16
# Write a function that test if a number is prime:

#     >>>isPrime(11)
#     >>>True
# Exercise 17
# Write a function that prints elements of a list if the index and the value are even:

#     >>>weirdPrint([1,2,2,3,4,5])
#     >>>[2,4]
# Exercise 18
# Write a function that accepts an undefined numbers of keyworded arguments and return the count of different types:

#     >>>TypeCount(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2
# Exercise 19
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.
# Exercise 20
#
# 

#  Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"

word = input("password")
def get_hidden(word):
    hidden_word =[]
    for letter in word:
        hidden_letter =letter.replace(letter,"*")
        hidden_word += hidden_letter
    print(hidden_word)

print(get_hidden(word))