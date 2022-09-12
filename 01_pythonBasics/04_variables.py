# Variables

#Storing data into a variable, used to invoke variables within the program/script/ etc
# Programs are simply data that's being stored, being changed, being removed.
# Variables can also be called names.

iq = 190
#assigning a value is also called 'binding'. In this example we are binding the value 190 to variabel 'iq'
#this number in memory get's stored as a binary representation in zeros and ones
print(iq)

#variables best practices
print('_______________________________________________')
print('VARIABLES BEST PRACTICES:')

print('-snake_case')
print('-start with lowercase or underscore')
print('-letters, numbers and underscores')
print('-cannot start a variable with a number')
print('-case sensitive')
print('-dont overwrite keywords')

user_iq = 190
_user_iq = 190
user_IQ = 190
print('_______________________________________________')

print('VARIABLES IN OPERATIONS/REASSIGN VARIABLES: ')
#can use variables in operations or to reassign variables

iq = 190
user_age = iq/4

print(user_age)
print('_______________________________________________')
print('VARIABLE CONSTANTS: ')
#constants
print('PI = 3.14')
PI = 3.14
print(PI)

#variable capitalized in good practice to show that the data should not be altered or changed
print('_______________________________________________')

print('RAPIDLY ASSIGN MULTIPLE VALUES TO VARIABLES: ')
#rapidly assign values to variables

a,b,c = 1, 2, 3
print(a)
print(b)
print(c)
