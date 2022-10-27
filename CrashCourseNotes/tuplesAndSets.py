# Tuple is a collection which is ordered and unchangable. allowd duplicate members.

# creating a tuple
# if i made it like this it will be considered as string
from typing import Tuple


wrongFruits = ('Apple')
fruits = ('Apple', )  # if we added , it will be considered as tuple
print(wrongFruits, type(wrongFruits))
print(fruits, type(fruits))

# lets work :D
# defining using the constructor
fruits = tuple(('Apples', 'Banana', 'Berries'))
print(fruits, type(fruits))


# we can't change the values like in the list
fruits[0] = 'Orange'  # => error

# but we can access the item
print(fruits[0])

# we can delete the whole tuple like this
del fruits

# print(fruits)  # it will tells you that fruits is not defined
fruits = tuple(('Apples', 'Banana', 'Berries'))

# getting the len
print(len(fruits))

'''
# Now lets see what are the sets
# Set : collection of items that are
    ## 1. unordered
    ## 2. unindexed -> to retrieve element you have to iterate -> [index] is not allowed
    ## 3. no duplicates are allowed
'''

# defining the set using {}
fruits_set = {'Apples', 'Oranges', 'Berries'}

# check whethere certain element exsits in the set
print('Apples' in fruits_set)

# Adding to the set
fruits_set.add('Grapes')
fruits_set.add('Apples')  # since it exists before it won't be added

# the order will differ in each runtime , but you will find only one apples
print(fruits_set)

# Removing from a set
fruits_set.remove('Oranges')  # I hate oranges :()
print(fruits_set)  # the order will differ in each runtime

# Clear the whole set
fruits_set.clear()

print(fruits_set)  # here we have empty set

# deleting a set
del fruits_set

# it will not be an empty, it frees the memory so it gives you an error
print(fruits_set)  # => error
