# we can use either '' or "" it doesn't matter.

name = 'Zizo'
age = '21'

# concatenation
# if we did this (+ age) we will get an error  so we must cast the int into str(age)
print('My name is ' + name + ' and my age is ' + str(age))


# Arguments by position
print('Hello, My Name is {esmy} and I am  {seny} years old.'.format(
    esmy=name, seny=age))


# F-String
print(f'Hello my name is {name}, and I am {age} years old')

# String methods
s = 'eh el kaLam, ya zmele?'
print(s.capitalize())

print(s.upper())  # all letters should be capital

print(s.lower())  # all should be lower
print(len(s))  # no of chars
print(s.swapcase())  # changes the case of the letters
print(s.replace('kaLam', 'KAlAm'))
print(s.count('lA'))  # btrg3 3dd el sub string el enta b3to
print(s.startswith('eh'))  # btrg3 bool true or false
# de btrg3 list bl kalemat, btfslhom b space da el default bs i think en aked mmkn nb3tlha redix 34an tfsl beh
print(s.split(sep=','))  # sep hwa da el delimeter el 3la asaso bn2sm el kalam
print(s.isalpha())  # true lw el string 7rof bs -> lw fe space htrg3 false
print(s.isnumeric())  # lw arkam bs
print(s.isalnum())  # lw eletnen
