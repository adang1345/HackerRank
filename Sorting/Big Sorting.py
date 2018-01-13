#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
# your code goes here
unsorted.sort(key=lambda x: len(x))
unsorted.sort(key=lambda x: int(x))
for x in unsorted:
    print(x)
