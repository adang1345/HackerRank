s = input().strip()
count = 0
for _ in range(50):
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            s = s[:i-1] + s[i+1:]
            break
if s:
    print(s)
else:
    print("Empty String")
