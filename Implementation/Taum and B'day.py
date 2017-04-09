#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    black_cost = b * min(x, y+z)
    white_cost = w * min(y, x+z)
    print(black_cost + white_cost)
