# A for loop in used for iterating over a sequence
# of elements (either list, tuple, dic, set, any iterable object or DS)

people = ['zizo', 'meme', 'noni', 'saso', 'hamdy']

# simple for loop
for person in people:
    print(f'Current person name is {person}')
    if(person == 'meme'):
        print('my best friend is here, say hello to him')
    elif(person == 'saso'):
        print('my girl bestfriend')


# for loops using range
for i in range(len(people)):
    print(people[i])

for i in range(0, 10, 3):  # here the range is from 0 to 10 - 1 and the step = 2
    print(i)

# while loops executes a certain code until a certain condition is violated

x = 11
while (x >= 0):
    print(x)
    x -= 3
