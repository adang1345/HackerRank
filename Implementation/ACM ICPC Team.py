#!/bin/python3

import sys
import itertools

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)

def topic_number(x, y):
    """Given bit strings x and y, return the number of topics known by x or y.
    Precondition: x and y have the same length."""
    c = 0
    for i in range(len(x)):
        if x[i] == "1" or y[i] == "1":
            c += 1
    return c

max_so_far = 0
num_max_so_far = 0
for x,y in itertools.combinations(topic, 2):
    t = topic_number(x, y)
    if t > max_so_far:
        max_so_far = t
        num_max_so_far = 1
    elif t == max_so_far:
        num_max_so_far += 1
print(max_so_far)
print(num_max_so_far)
