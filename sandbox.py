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


arr = [1, 2, 3, 10, 0]
push_down(arr, 4)
print(arr)
