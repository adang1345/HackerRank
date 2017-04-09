#!/bin/python3

import sys


s = input().strip()
c = 0
for n in range(len(s)):
    i = n % 3
    if i == 0 and s[n] != "S" or i == 1 and s[n] != "O" or i == 2 and s[n] != "S":
        c += 1
print(c)
