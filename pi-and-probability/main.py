#!/usr/bin/env python3

# This is the old code, when I still was a kid. This program was realized with the help of my middle school math teach prof. Guzzardi.
# (this program is unnecessarly long and badly written)

import random

def rock():
    # random coordinates of the falling point of the rock
    x = random.randint(0,1000)                                                                                               
    y = random.randint(0,1000)

    # if the rock fall in the bucket
    if x*x + y*y <= 1000000:
        return 1
    else:
        return 0

def bucket(n):
    j = 0
                                                                                                                             
    # for n times throw the rock and count how many were sucessfull
    for i in range(n):
        j = rock()+j
    return j

def area():
    # inverse formula of the circle area 
    a = 4*bucket(1000000)/1000000
    return a

print(area())
