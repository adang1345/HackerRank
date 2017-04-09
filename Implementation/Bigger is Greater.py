def swap(a, i, j):
    """Swap a[i] and a[j]."""
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def next_string(w):
    """Given a string w, return the smallest permutation of w that is lexicographically greater than w. If none exists, then
    return "no answer".
    Precondition: len(w) > 0"""
    w = list(w)
    i = len(w) - 1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1
    if i == 0:
        return "no answer"
    pivot = i - 1
    succ = len(w)-1
    while w[succ] <= w[pivot]:
        succ -= 1
    swap(w, pivot, succ)
    reverse_suffix = reversed(w[i:])
    w = w[:i] + list(reverse_suffix)
    return "".join(w)


t = int(input().strip())
for _ in range(t):
    w = input().strip()
    n = next_string(w)
    print(n)
