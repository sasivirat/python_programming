# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:21:03 2024

@author: Sasi Kishore Varma

"""

def hello():
    '''
    This is the docstring.
    '''
    print('Hello, world!')
    
def hi(name):
    print(f'Hello, {name}!')

def hi_2(name='Giles'):
    print(f'Hello, {name}!')   
    
def fib_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_2(n-1) + fib_2(n-2)
    
def fib(n):
    
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a+b
    return a    