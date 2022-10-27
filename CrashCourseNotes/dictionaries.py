''' 
    A dictionary is a collection of items which are
        1. unordered 
        2. changable 
        3. indexed
        4. no duplicates are allowed

    dictionaries are just map in c++. 
'''

# Creating a dictionary
person = {
    'firstName': 'Abdelaziz',
    'LastName': 'Salah',
    'age': 21
}

# using constructor
person2 = dict(first_Name='Esraa', last_Name='Mamdoh',
               pos='myBestiie')  # we define key = value

# this is how we print the whole dicts
print(person, person2)

# print certain value of certain key
print(person['firstName'])
print(person2['pos'])
# print(person2['somethingDoesn\'tExist'])  # => gives keyError


# accessing element using getter
print(person.get('age'))


# adding key/Value
person['specialization'] = 'Computer Engineering'
print(person['specialization'])


# get the dict all keys
print(person2.keys())

# get the dict all values
print(person2.values())

# copying a whole dict in another one
person3 = person2.copy()
person3['role'] = 'sabre Fencer'
print(person2, person3)

# remove an item
del (person3['role'])
print(person3)

# we can use pop instead of del
person3.pop('last_Name')
print(person3)

# clearing the whole dict
person3.clear()
print(person3)

# getting the len
print(len(person))

# we can have list of dicts and dict of string key and list value, we can do whatever we want.
people = [
    person,
    person2,
    person3
]

print(people)
