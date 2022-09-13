#TYPE CONVERSION

print('CONVERTING 100 INTO A STRING')
print(type(str(100)))

print('CONVERTING 100 INTO A STRING AND THEN AN INTEGER')
print(type(int(str(100))))

print('USING VARIABLES WITH CONVERSIONS')
a = str(100)
b = int(a)
c = type(b)
print(c)
