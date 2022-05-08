#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#all functions return a value

def function(n): #required arguments seperated by commas in ()
    print(n*2)     #variables within function

function(47)

#use default value for argument
def testfunction(n=1):
    print(n)  

testfunction(4)
testfunction()
