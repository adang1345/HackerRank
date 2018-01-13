#!/bin/python3

import sys


def solve(year):
    """Return the date of the 256th day of the year in Russia in the format dd.mm.yyyy."""
    if year <= 1917:  # use Julian calendar
        return "{}.09.{}".format(12 if year % 4 == 0 else 13, year)
    elif year == 1918:
        return "26.09.1918"
    else:
        return "{}.09.{}".format(12 if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 13, year)

year = int(input().strip())
result = solve(year)
print(result)
