n = int(input().strip())
intersect = set("abcdefghijklmnopqrstuvwxyz")

for _ in range(n):
    s = input().strip()
    intersect = intersect.intersection(set(s))

print(len(intersect))
