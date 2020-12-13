# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:48:03 2020

@author: eliza
"""

import math


#largest prime factor of 600851475143

#number 
number = input("Enter a number: ")
n = int(number)     

#initial largest prime factor is 1
lpf = 1

#check if divisible by 2

while (n % 2 == 0):
    lpf = 2
    n = n / 2
    
#rounds down for square root
for i in range(3,int(math.sqrt(n))+1):
    while (n % i == 0):
        lpf = i
        n = n/i
        
print("The largest prime factor is:", lpf)



