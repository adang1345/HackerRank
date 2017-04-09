#!/bin/python3

import sys
import math


s = input().strip()
rows = int(math.sqrt(len(s)))
columns = math.ceil(math.sqrt(len(s)))
if rows*columns < len(s):
    rows += 1
p = ""
for i in range(columns):
    for j in range(rows):
        next_index = i + columns * j
        if next_index < len(s):
            p += s[next_index]
    p += " "
print(p[:-1])
