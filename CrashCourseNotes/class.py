'''
    a class is a blue print for creating objects. 
    each object has certain properties which diffrentiate him from the other, 
    but all objects have certain main properties. 

    ie: all of us are humans, all of us has names, age, position, friends ... (friends! shit)
    so the basics are same but the values of these basics are the things which diffrentiate 
    each person from the other. 

    so for me 
    my name is Abdelaziz, but maybe you are not Abdelaziz, 
    I am 21, you maybe above 30, and so on, i wish you got me. 


    also we can define some functions for each class, as getters and setters and custom functions to be called
    in order to be able to access the properties of each class object, 
    
    ie: we can have function called get_name which prints the object name
    Abdelaziz.get_name() -> Abdelaziz.... very obvious. 
'''

# creating a class


class person:
    # self is must be sent to indicate that we are appling the operations on this object not
    # different one
    def __init__(self, name, age, pos):
        self.name = name
        self.age = age
        self.pos = pos

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getPos(self):
        return self.pos


zizo = person('Abdelaziz', 21, 'Student')

print(zizo.getName())
print(zizo.getAge())
print(zizo.getPos())
