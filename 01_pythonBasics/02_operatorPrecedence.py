#Operator Precedence
#Different operator has precedence over others
print('_______________________________________________')

print('Order Precedence')

# ()
# **
# * /
# + -

print('01. ()')
print('02. **')
print('03. * /')
print('04. + -')

print('print((20-3)+ 2 ** 2)')
print((20-3)+ 2 ** 2)
#Brackets will come first and then the power
print('Brackets will come first and then the power - Because of order of precedence.')

print('_______________________________________________')

print('Order Precedence - Assignment')

# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2) # 45.0 (float)
#(5+4), * 10, then / 2

print(((5 + 4) * 10) / 2) # 45.0 (float)
#(5+4), * 10, then / 2

print((5 + 4) * (10 / 2)) # 45.0 (float)
#(5+4), then (10/2), 9 * 5

print(5 + (4 * 10) / 2) # 25.0 (float)
#(4*10), 40 / 2 , 20 + 5

print(5 + 4 * 10 // 2) # 25 (int)
# 4 * 10, then 40 // 2, 20 + 5
