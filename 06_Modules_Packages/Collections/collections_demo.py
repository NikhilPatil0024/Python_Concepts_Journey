"""collections: Counter, defaultdict, deque, namedtuple."""
from collections import Counter, defaultdict, deque, namedtuple
print(Counter("mississippi"))
d = defaultdict(int)
d["x"] += 1
print(d)
q = deque([1,2,3]); q.appendleft(0); q.pop(); print(q)
Point = namedtuple("Point", "x y"); print(Point(2,3))
