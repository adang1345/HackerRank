#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
rotated = ""

for char in s:
    if char.isalpha():
        if char.islower():
            rotated += lower[(lower.index(char)+k) % 26]
        else:
            rotated += upper[(upper.index(char)+k) % 26]
    else:
        rotated += char
print(rotated)
