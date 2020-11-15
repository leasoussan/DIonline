# revers sentence 
# # to avoid repetition 

# 1 Put sentence in a list 

# 2 loop through 

# solution 1
sentence = "this is a test sentence"
my_list = sentence.split(" ")

# sentence = "this is a test sentence".split("")

my_list.reverse()
print(my_list)



# solution 2
sentence = "this is a test sentence".split("")
my_list = sentence.split("")
rev_list = []

for i in range(len(my_list)-1, -1, -1))
    rev_list.append(my_list[i])

print(" ".join(rev_list))


# list.reverse()
# loop backword range(start, stop, step)
# dont take user input until you are ready 
