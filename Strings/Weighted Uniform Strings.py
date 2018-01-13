#!/bin/python3

import sys


def letter2weight(l):
    """Return the weight of letter l.
    Precondition: l is a string consisting of exactly 1 lowercase letter"""
    return ord(l) - 96


def uniform_str_weights(s):
    """Return a set of all uniform string weights of s."""
    i = 0
    j = 0
    w = set()
    while j < len(s):
        if s[i] == s[j]:
            w.add(letter2weight(s[i]) * (j-i+1))
            j += 1
        else:
            i = j
    return w


s = input().strip()
n = int(input().strip())
u = uniform_str_weights(s)

for a0 in range(n):
    x = int(input().strip())
    # your code goes here

    if x in u:
        print("Yes")
    else:
        print("No")
