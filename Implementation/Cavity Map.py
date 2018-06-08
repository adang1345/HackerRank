#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    for i in range(1, n-1):
        for j in range(1, n-1):
            if grid[i-1][j] != "X" and grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and \
                    grid[i][j-1] != "X" and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
                grid[i][j] = "X"
    return map(lambda row: "".join(map(str, row)), grid)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = list(map(int, input()))
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
