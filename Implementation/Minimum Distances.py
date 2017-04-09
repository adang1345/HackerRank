#!/bin/python3

import sys


n = int(input().strip())
a = [int(A_temp) for A_temp in input().strip().split(' ')]

min_dist = len(a)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j] and j-i < min_dist:
            min_dist = j - i
            break
if min_dist == len(a):
    print(-1)
else:
    print(min_dist)
