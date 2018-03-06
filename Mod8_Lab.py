#!/usr/bin/env python3
'''
Module 8 - Lab 1
2 2 unread replies. 2 2 replies.
For this lab we're going to create a calculator:

Create a class called "Calculate"
Add methods to add, subtract, divide and multiply two numbers
Instantiate the class and use each method
Post your code to the discussion page for credit
'''
class Calculator():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_two(self, x, y):
        adds = (self.x + self.y)
        return adds

    def sub_two(self, x, y):
        subs = (self.x - self.y)
        return subs

    def div_two(self, x, y):
        divs = (self.x / self.y)
        return divs

    def mult_two(self, x, y):
        mults = (self.x * self.y)
        return mults

calc1 = Calculator(20, 15)
print(calc1.add_two(20, 15))


