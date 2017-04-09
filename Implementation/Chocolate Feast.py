#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    chocolate = n // c
    total_chocolate = chocolate
    wrappers = chocolate
    while wrappers >= m:
        chocolate = wrappers // m
        wrappers = wrappers % m + chocolate
        total_chocolate += chocolate
    print(total_chocolate)
