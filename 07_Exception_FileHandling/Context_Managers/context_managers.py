"""Custom context manager via class and contextlib."""
class Resource:
    def __enter__(self):
        print("acquire")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("release")
with Resource() as r:
    print("using resource")

from contextlib import contextmanager
@contextmanager
def timer():
    import time
    t0 = time.time()
    try:
        yield
    finally:
        print(f"elapsed: {time.time()-t0:.6f}s")
with timer():
    sum(range(1000000))
