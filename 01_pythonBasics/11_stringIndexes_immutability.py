#STRING INDEXES

string_index = '01234567'
            #   01234567

print('STRING SLICING')
#STRING SLICING

# [START:STOP]
print('print(string_index[0:3])')
print(string_index[0:3])
print('ANSWER: 012')

print('print(string_index[0:7])')
print(string_index[0:7])
print('ANSWER: 0123456')

# [START:STOP:STEPOVER]
print('print(string_index[0:7:2])')
print(string_index[0:7:2])
print('ANSWER: 0246')

# ALSO VALID
print('print(string_index[1:])')
print(string_index[1:])
print('ANSWER: 1234567')
print('print(string_index[:5])')
print(string_index[:5])
print('ANSWER: 01234')
print('print(string_index[::2])')
print(string_index[::2])
print('ANSWER: 0246')

#NEGATIVE INDEX - TO START AT THE END OF THE STRING
print('NEGATIVE INDEX')
print(string_index[-1])
print(string_index[-2])
print(string_index[-3])
print(string_index[::-1])

#IMMUTABILITY

#STRINGS IN PYTHON ARE IMMUTABLE - THIS MEANS THEY CANNOT BE CHANGED

string_index = '01234567'
#THIS WILL NOT WORK - STRINGS ARE IMMUTABLE
# string_index[0] = '8'
print("string_index[0] = '8'")
#THE ONLY WAY TO CHANGE STRING_INDEX IS TO REASSIGN THE VALUE

#CAN DO
string_index = string_index + '8'

print(string_index)
