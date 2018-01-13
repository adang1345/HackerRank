p = int(input().strip())

for _ in range(p):
    a = set(input().strip())
    b = set(input().strip())

    for x in a:
        if x in b:
            print("YES")
            break
    else:
        print("NO")
