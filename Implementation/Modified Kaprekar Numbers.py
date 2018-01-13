def new_int(n):
    """Cast string n to an int. If n is empty, return 0."""
    if not n:
        return 0
    else:
        return int(n)


def is_kaprekar(n):
    """Return whether n is a modified Kaprekar number."""
    d = len(str(n))
    square = str(n ** 2)
    return new_int(square[-d:]) + new_int(square[:-d]) == n


p, q = int(input().strip()), int(input().strip())
kaprekar_nums = list(filter(is_kaprekar, range(p, q+1)))
if kaprekar_nums:
    print(" ".join(map(str, kaprekar_nums)))
else:
    print("INVALID RANGE")
