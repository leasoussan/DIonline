# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then:
# 2 Display him a little cake, like this:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles should be the last cypher of his age, if he is 53, then add 3 candles.

# If he was born on a leap year, display two cakes !
cake= """:\n  ___iiiii___
  |:H:a:p:p:y:|
__|___________|__
|^^^^^^^^^^^^^^^^^|
|:B:i:r:t:h:d:a:y:|
|                 |
~~~~~~~~~~~~~~~~~~~"""


given_dob =input("what's your birthday??DD/MM/YYYY")

year = given_dob[-4:]
calc_year = int(year)

print (calc_year)
if calc_year %2 == 0:
    print(cake * 2 )
else :
    print(cake)

# actions
# het DOB- and convert into a list -collect the 4 last numbers 
# if year %2 = 0 then show him 2 cacks
