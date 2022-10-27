# python has functions for creating, reading, updating and deleting files

# open files
myFile = open('myFile.txt', 'w')  # file name , mode (w) -> write

# Get some info
print(f'Name: {myFile.name}')
print(f'Name: {myFile.closed}')
print(f'Name: {myFile.mode}')

# Writing into files
myFile.write('I love python')
myFile.write(' and I love flutter')
myFile.close()

# Append file
myFile = open('myFile.txt', 'a')
myFile.write('I love all programming')
myFile.write(' and I love flutter again')
myFile.close()

# Reading file
myFile = open('myFile.txt', 'r')
text = myFile.read(100)
print(text)
