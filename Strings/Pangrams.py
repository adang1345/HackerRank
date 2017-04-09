s = input().strip().lower()

contains_letter = [False] * 26
for x in s:
    if x != " ":
        contains_letter[ord(x)-97] = True
if all(contains_letter):
    print("pangram")
else:
    print("not pangram")
