s = input().strip()

s_dict = {}
for x in s:
    if x in s_dict:
        s_dict[x] += 1
    else:
        s_dict[x] = 1

num_odd = 0
for x in s_dict:
    if s_dict[x] % 2 == 1:
        num_odd += 1
    if num_odd == 2:
        print("NO")
        exit(0)
print("YES")
