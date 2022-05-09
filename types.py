#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
print('x is {}'.format(x))
# same as "f string - avail 3.6 and after"
print(f'x is {x}')

#what is the data type of the variable x
print(type(x))

y = 'word'
print(type(y))

z = 3.0
print(type(z))

#stings on multiple lines
w = '''
one
two
three'''
print(w)

#strings are objects
x='word'
print(x.capitalize())
print(x.upper())

x='seven {} {}'.format('8', 9)
print('x is {}'.format(x))
print(f'x is {x}')

# change position of {}
x='seven {1} {0}'.format('8', 9)
print('Change position: x is {}'.format(x))
print(f'x is {x}')

#and add spaces to left(<) or right(>) of position 
x='seven {0:<10} - {1:>10}'.format('8', 9)
print('add spaces to left(<) or right(>): x is {}'.format(x))
print(f'x is {x}')

#and add characters to left(<) or right(>) of position 
x='seven {0:<010} - {1:>010}'.format('8', 9)
print('add chafracters to left(<) or right(>): x is {}'.format(x))
print(f'x is {x}')

a = 8
b = 9
x = f'using f strings: {a:5} - {b:05}'
print(x)

#python 3 changed divion to floats
x = 7/3
print(f'divided numbers with / become float: {x} :' +str(type(x)) )
x = 7//3
print(f'divided numbers with // become int: {x} :' +str(type(x)) )

#floating point do not work with money
#Can get  something like 5.551115123125783e-17
x = .1+.1+.1-.3
print(x)
print(type(x))
#solve with decimal library:
from decimal import Decimal
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print(f'Using decimal import : {x}')
print(type(x))

