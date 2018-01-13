d = int(input().split()[1])
a = set(map(int, input().split()))
c = 0
for i in a:
    if (i + d) in a and (i + 2*d) in a:
        c += 1
print(c)
