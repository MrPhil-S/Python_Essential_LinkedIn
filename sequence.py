#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


#square brackets - creates a list
x = [ 1, 2, 3, 4, 5, ]
for i in x:
    print('i is {}'.format(i))

# list is mutable (can be changed)
x = [ 1, 2, 3, 4, 5 ]
x[2] = 100
for i in x:
    print('i is {}'.format(i))

#tuple uses parenthises and is immutable
x = ( 1, 2, 3, 4, 5 )
x[2] = 100
for i in x:
    print('i is {}'.format(i))

