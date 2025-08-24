"""Function decorator with wraps."""
import time, functools
def timing(fn):
    @functools.wraps(fn)
    def wrapper(*a, **k):
        t0=time.time()
        try:
            return fn(*a, **k)
        finally:
            print(f"{fn.__name__} took {time.time()-t0:.6f}s")
    return wrapper

@timing
def work(n):
    s = 0
    for i in range(n): s += i
    return s

print(work(100000))
