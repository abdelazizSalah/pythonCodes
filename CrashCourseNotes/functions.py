'''
    function is a block of code which runs only when it is excuted or called. 
    here we don't use curly braces {} for functions we use : and intendations <= they are very
    senstive in python so be carefull.
'''

# Creating a function


# we define a default value to avoid errors
def sayHello(name='Person'):
    print(f'Hello {name}')


# Return values
def getSum(num1, num2):
    return num1 + num2


'''
    lambda function is a small function which is anonymous. 
    it can take any number of arguments, but can only have one expression.
    very similar to darts arrow function, actually they may be the same.  
'''
getDif = lambda num2, num1 : num2 - num1

# calling the function we created
print(getDif(4,1))
print(getSum(1, 5))
sayHello()
