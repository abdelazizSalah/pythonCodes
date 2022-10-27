# if/Else applying some codes depending on whethere the condition is true or false
x = 10
y = 5

# Comparison operators (== , >= , <= , > , <, !=)
if(x != y):
    print('They are different!')
else:
    print('They are identical!')


# Logical operators (and, or, not)
if(not x == y and x > y):
    print('They are different! and x greater than y')
elif(not x == y or y < x):  # else if
    print('they are either different or y less than x ')


# membership operators (in, not in)
# they are usually used to test if a sequence is presented in an object or not
newlist = [3, 2, 1, 6, 3]

print(5 in newlist)
print(5 not in newlist)
print([3, 2, 1] in newlist)  # do you think it will be true or false ?

# identity operators (is, is not)
# usually used to compare objects of the same class
x = 3.2
if(x is int):
    print('x is not float guys!')
else:  # similar to (x is not int)
    print(f'x is {type(x)}')
