#AUGMENTED ASSIGNMENT OPERATOR

#Variable MUST be defined before using augmented assignment operator

some_value = 5
some_value = some_value + 2
print('some_value = 5')
print('some_value = some_value + 2')
print('This is NOT using Augmented Assignment Operator: ')
print(some_value)

print('_______________________________________________')
#instead we can use the augmented assignment operator

some_value = 5
some_value += 2
print('some_value = 5')
print('some_value += 2')
print('This is using Augmented Assignment Operator: ')
print(some_value)

#can also change it to '-=' to subtract

# +=
# -=
# *=
print('_______________________________________________')
print('AUGMENTED ASSIGNMENT OPERATOR ASSIGNMENT: ')


counter = 0

counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *=2

#Before you click RUN, guess what the counter variable holds in memory!
print(counter)
