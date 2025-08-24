"""Coroutine basics with send()."""
def consumer():
    total = 0
    try:
        while True:
            x = (yield total)
            total += x
    except GeneratorExit:
        pass
c = consumer(); print(next(c))
print(c.send(5)); print(c.send(7)); c.close()
