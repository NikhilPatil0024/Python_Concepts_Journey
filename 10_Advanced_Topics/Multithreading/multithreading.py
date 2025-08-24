"""Threading with locks to protect shared state."""
import threading
lock = threading.Lock()
counter = 0
def work(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1
threads = [threading.Thread(target=work, args=(1000,)) for _ in range(4)]
[t.start() for t in threads]
[t.join() for t in threads]
print("counter:", counter)
