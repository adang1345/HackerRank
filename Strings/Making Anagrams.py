a = input().strip()
b = input().strip()

s = 0
a_dict = {}
for x in a:
    if x in a_dict:
        a_dict[x] += 1
    else:
        a_dict[x] = 1
b_dict = {}
for x in b:
    if x in b_dict:
        b_dict[x] += 1
    else:
        b_dict[x] = 1

for x in a_dict:
    if x in b_dict:
        s += max(a_dict[x] - b_dict[x], 0)
    else:
        s += a_dict[x]
for x in b_dict:
    if x in a_dict:
        s += max(b_dict[x] - a_dict[x], 0)
    else:
        s += b_dict[x]
print(s)
