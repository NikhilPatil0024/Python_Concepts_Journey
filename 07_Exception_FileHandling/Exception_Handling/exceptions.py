"""try/except/else/finally and custom exception."""
class MyError(Exception): pass
def risky(x):
    if x < 0: raise MyError("negative!")
    return x**0.5
try:
    print(risky(4))
    print(risky(-1))
except MyError as e:
    print("Handled:", e)
else:
    print("No exception")
finally:
    print("Always runs")
