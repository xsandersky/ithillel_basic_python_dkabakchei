#1.a
a = 5
b = 7
c = a
a = b
b = c
print('1.a = ', a, b)

#1.b
a = 5
b = 7
a, b = b, a
print('1.b = ', a, b)

#1.c
a = 5
b = 7
c = b
b = c - b + a
a = a - b + c
print('1.c = ', a, b)