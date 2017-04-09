#!/bin/python3

import sys


h = int(input().strip())
m = int(input().strip())

def words(n):
    """Return the word form of an integer n in 1..99"""
    if n == 0:
        return ""
    small = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
              "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    large = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n < 20:
        return small[n-1]
    return large[n//10-2] + " " + words(n%10)

if m == 0:
    print(words(h) + " o' clock")
elif m < 30 and m != 15:
    print(words(m) + " minutes past " + words(h))
elif m == 15:
    print("quarter past " + words(h))
elif m == 30:
    print("half past " + words(h))
elif m != 45:
    print(words(60-m) + " minutes to " + words(h+1))
else:
    print("quarter to " + words(h+1))
