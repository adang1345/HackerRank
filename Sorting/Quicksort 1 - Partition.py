input()
arr = [int(x) for x in input().split()]
lower = []
upper = []
p = arr[0]
for x in arr[1:]:
    if x <= p:
        lower.append(x)
    else:
        upper.append(x)
partitioned = lower + [p] + upper
print(" ".join(map(str, partitioned)))
