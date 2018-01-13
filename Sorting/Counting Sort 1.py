#!/bin/python3

import sys

def countingSort(arr):
    counts = [0] * 100
    for n in arr:
        counts[n] += 1
    return counts

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))
