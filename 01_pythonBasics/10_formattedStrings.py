#FORMATTED STRINGS

name = 'Danielle'
age = 27

#NOT A FORMATTED STRING
print('hi ' + name + '. You are ' + str(age) + ' years old.' )

# A FORMATTED STRING
print(f'hi {name}. You are {age} years old.')

#ORIGINAL FORMAT IN PYTHON 2
print('hi {name}. You are {age} years old.'.format(name, age))

#SWITCHING UP THE VARIABLES
print('hi {1}. You are {0} years old.'.format(name, age))
