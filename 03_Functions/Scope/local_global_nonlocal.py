"""Local, global, nonlocal scopes."""
x = "global"
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    return x
print(x, outer())
