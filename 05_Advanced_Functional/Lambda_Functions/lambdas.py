"""Anonymous functions with lambda."""
xs = [("a",3),("b",1),("c",2)]
xs.sort(key=lambda kv: kv[1])
print(xs)
