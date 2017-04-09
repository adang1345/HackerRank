import functools

@functools.lru_cache(maxsize=None)
def mod_fib(n, t1, t2):
    if n == 1:
        return t1
    elif n == 2:
        return t2
    return mod_fib(n-2, t1, t2) + mod_fib(n-1, t1, t2)**2

t1,t2,n = map(int, input().split())
print(mod_fib(n, t1, t2))
