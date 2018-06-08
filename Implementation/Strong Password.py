#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    c = 0
    if not any(map(str.isdigit, password)):
        c += 1
    if not any(map(str.islower, password)):
        c += 1
    if not any(map(str.isupper, password)):
        c += 1
    if not any(map(lambda char: char in "!@#$%^&*()-+", password)):
        c += 1
    if n + c < 6:
        c += 6 - n - c
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
