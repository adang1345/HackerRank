input()
arr = [int(x) for x in input().split()]

def swap(arr, a, b):
    """Swap values at arr[a] and arr[b]."""
    arr[a],arr[b] = arr[b],arr[a]

def push_down(arr, i):
    """Push arr[i] down to its sorted position.
    Precondition: i > 1"""
    j = i - 1
    while arr[j] > arr[i] and j >= 0:
        swap(arr, j, i)
        i -= 1
        j -= 1

for i in range(1, len(arr)):
    push_down(arr, i)
    print(" ".join(str(x) for x in arr))
