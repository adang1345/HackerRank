#!/bin/python3

import sys


def common_len(s, t):
    """Return the length of the longest string that is at the beginning of both s and t.
    Precondition: s and t are non-empty strings"""
    cl = 0
    while s[cl] == t[cl]:
        cl += 1
        if cl == len(s) or cl == len(t):
            break
    return cl


s = input().strip()
t = input().strip()
k = int(input().strip())

if len(s) + len(t) - 2 * common_len(s, t) > k:  # s and t have lengths that are too different
    print("No")
elif k % 2 == (len(s) + len(t) - 2 * common_len(s, t)) % 2:  # k has same parity as direct conversion from s to t
    print("Yes")
elif len(s) + len(t) <= k:  # convert s to empty string
    print("Yes")
else:
    print("No")
