#!/bin/python3

import sys


s = input().strip()
c = 1
for x in s:
    if x.isupper():
        c += 1
print(c)
