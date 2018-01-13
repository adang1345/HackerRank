s = input().strip()


def near_valid(d):
    """Given a dictionary d describing the count of each letter in a string, return whether it is possible to remove
    <=1 character from the string to make the string valid."""
    count_of_counts = {}
    for x in d.values():
        if x in count_of_counts:
            count_of_counts[x] += 1
        else:
            count_of_counts[x] = 1
    if len(count_of_counts) > 2:
        return False
    if len(count_of_counts) == 1 or 1 in count_of_counts and count_of_counts[1] == 1:
        return True
    if 1 not in count_of_counts.values():
        return False
    one_key = None
    other_key = None
    for x in count_of_counts:
        if count_of_counts[x] == 1:
            one_key = x
        else:
            other_key = x
    return one_key == other_key + 1


s_dict = {}
for x in s:
    if x in s_dict:
        s_dict[x] += 1
    else:
        s_dict[x] = 1
# print(s_dict)
if near_valid(s_dict):
    print("YES")
else:
    print("NO")
