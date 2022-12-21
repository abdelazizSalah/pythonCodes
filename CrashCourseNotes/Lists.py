# Creating a list
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'grapes', 'kiwi']
# using a constructor
numbers2 = list((1, 2, 3, 4, 5))
print(numbers2)

# getting a value
print(fruits[2])  # it works 0 based

# getting the len
print(len(fruits))

# Appending to a list
fruits.append('Mango')
print(fruits)

# remove stuffs using name
fruits.remove('grapes')
print(fruits)

# insert into certain pos
fruits.insert(1, 'Strawberries')
print(fruits)

# remove from certain index
fruits.pop(2)
print(fruits)

# change variables in certain postion
fruits[0] = 'Banana'
print(fruits)


# how to create 2d array
