n = int(input().strip())

for _ in range(n):
    s = input().strip()
    d = []
    for find in ("A", "B"):
        d1 = 0
        i = 0
        while i < len(s):
            if s[i] != find:
                d1 += 1
            elif find == "A":
                find = "B"
            else:
                find = "A"
            i += 1
        d.append(d1)
    print(min(d))
