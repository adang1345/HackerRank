#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
queen = [int(rQueen),int(cQueen)]
obstacles = []
for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    obstacles.append((rObstacle,cObstacle))

def obstacle_type(queen,obstacle):
    """Given coordinates of queen and an obstacle, return the type of obstacle.
    -1: not an obstacle for the queen
    0: up
    1: up-right
    2: right
    3: right-down
    4: down
    5: down-left
    6: left
    7: left-up"""
    if queen[0] < obstacle[0] and queen[1] == obstacle[1]:
        return 0
    elif queen[0] < obstacle[0] and obstacle[0]-queen[0] == obstacle[1]-queen[1]:
        return 1
    elif queen[0] == obstacle[0] and obstacle[1] > queen[1]:
        return 2
    elif queen[0] > obstacle[0] and queen[0]-obstacle[0] == obstacle[1]-queen[1]:
        return 3
    elif queen[0] > obstacle[0] and queen[1] == obstacle[1]:
        return 4
    elif queen[0] > obstacle[0] and obstacle[0]-queen[0] == obstacle[1]-queen[1]:
        return 5
    elif queen[0] == obstacle[0] and obstacle[1] < queen[1]:
        return 6
    elif queen[0] < obstacle[0] and queen[0]-obstacle[0] == obstacle[1]-queen[1]:
        return 7
    else:
        return -1

def dist(a, b):
    """Return the chessboard distance between 2D points a and b. I define the chessboard distance as the max of the difference
    in row and the difference in column."""
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

def closest_obstacles(queen, obstacles):
    """Return a list of obstacles closest to the queen in all 8 directions. A direction that has no obstacles is represented as
    (0,0)."""
    closest = [(0,0)]*8
    for obstacle in obstacles:
        t = obstacle_type(queen, obstacle)
        if t > -1 and closest[t] == (0,0):
            closest[t] = obstacle
        elif t > -1 and dist(queen,obstacle) < dist(queen,closest[t]):
            closest[t] = obstacle
    return closest

closest = closest_obstacles(queen, obstacles)

# up
if closest[0] == (0,0):
    up = n - queen[0]
else:
    up = dist(closest[0], queen) - 1

# up_right
if closest[1] == (0,0):
    up_right = min(n-queen[0], n-queen[1])
else:
    up_right = dist(closest[1], queen) - 1

# right
if closest[2] == (0,0):
    right = n - queen[1]
else:
    right = dist(closest[2], queen) - 1

# right_down
if closest[3] == (0,0):
    right_down = min(queen[0]-1, n-queen[1])
else:
    right_down = dist(closest[3], queen) - 1

# down
if closest[4] == (0,0):
    down = queen[0] - 1
else:
    down = dist(closest[4], queen) - 1

# down_left
if closest[5] == (0,0):
    down_left = min(queen[0]-1, queen[1]-1)
else:
    down_left = dist(closest[5], queen) - 1

# left
if closest[6] == (0,0):
    left = queen[1] - 1
else:
    left = dist(closest[6], queen) - 1

# left_up
if closest[7] == (0,0):
    left_up = min(n-queen[0], queen[1]-1)
else:
    left_up = dist(closest[7], queen) - 1

print(up + up_right + right + right_down + down + down_left + left + left_up)
