#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'quaaaak'
    walking = 'walks like a duck'

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


    # def quack(self):
    #     print('Quaaack!')

    # def walk(self):
    #     print('Walks like a duck.')



def main():
    #Duck().quack()
    #Duck().walk()
    donald = Duck()
    donald.quack()
    donald.walk()

class Tree:
   height=5
   def Height(self):
       print('heights is {}'.format(self.height))
Elm=Tree()
Elm.Height()



if __name__ == '__main__': main()
