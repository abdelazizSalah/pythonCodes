'''
    a module is basicly a python file which contains some static data members and functions which
    you can use them without needing to implement their logic from the scratch
    you can call them libraries also.  
'''

import numpy as np
import pandas

# pip module
from camelcase import CamelCase

# import custom modules
import validator

# here I am just importing certain function from the whole function,
# which is better to enhance the performance instead of loading the whole file which you are not
# going to use most of its functions you can simply import the functions you need
from numpy import abs


# the pip
'''
    pip is the python packages installer 
    which is a package manager by which you can
    deal with all the packages. 

    so you can install packages, delete some, upgrade, or even check they do exits. 
    all of this pip is the responsible for them.

    something like gcc in c and g++ in c++
'''

# it converts each first letter into capital one
c = CamelCase()
print(c.hump('hello my frined'))

# this should return false
print(validator.validate_email_address('Abdelaziz132001@mail..com'))

# this should return true
print(validator.validate_email_address('Abdelaziz132001@gmail.com'))
