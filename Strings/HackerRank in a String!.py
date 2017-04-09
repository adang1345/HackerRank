#!/bin/python3

import sys


q = int(input().strip())
h = "hackerrank"
for a0 in range(q):
    s = input().strip()
    j = 0
    for i in range(len(s)):
        if s[i] == h[j]:
            j += 1
        if j == len(h):
            break
    if j == len(h):
        print("YES")
    else:
        print("NO")
