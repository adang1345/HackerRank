#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    left_dist = []
    right_dist = []
    last_station = -1
    for i in range(n):
        if i in c:
            last_station = i
        left_dist.append(float("inf") if last_station == -1 else i - last_station)
    last_station = -1
    for i in range(n-1, -1, -1):
        if i in c:
            last_station = i
        right_dist.append(float("inf") if last_station == -1 else last_station - i)
    return max(map(min, zip(left_dist, reversed(right_dist))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = set(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
