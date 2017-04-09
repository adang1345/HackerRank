def is_funny(s):
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(r[i])-ord(r[i-1])):
            return False
    return True

t = int(input().strip())
for _ in range(t):
    if is_funny(input().strip()):
        print("Funny")
    else:
        print("Not Funny")
