# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:43:37 2020

@author: eliza
"""


#a^2 + b^2 = c^2
#a + b + c = 1000

#a, b, c must be ints

#a < 999
#b < 999
#1 < c < 999

sum = 0 

for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(2, 1000):
            sum = a + b + c
            LHS = a**2 + b**2
            RHS = c**2
            if ((sum == 1000) and (LHS == RHS)):
                print("Values of a, b, c:", a, b, c)
                
                