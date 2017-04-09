input()
arr = [int(x) for x in input().split()]

e = arr[-1]
i = len(arr) - 2
while arr[i] > e and i >= 0:
    arr[i+1] = arr[i]
    i -= 1
    print(" ".join(str(x) for x in arr))
arr[i+1] = e
print(" ".join(str(x) for x in arr))
