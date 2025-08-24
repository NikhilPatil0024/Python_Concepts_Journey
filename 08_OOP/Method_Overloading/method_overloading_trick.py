"""Python doesn't have true overloading; use defaults or singledispatch."""
from functools import singledispatch
@singledispatch
def show(x): return f"default:{x}"
@show.register(int)
def _(x:int): return f"int:{x}"
@show.register(str)
def _(x:str): return f"str:{x}"
print(show(10), show("hi"), show(3.14))
