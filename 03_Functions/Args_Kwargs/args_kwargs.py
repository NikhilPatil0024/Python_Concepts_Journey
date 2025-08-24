"""Variable-length args (*args) and kwargs (**kwargs)."""
def summarize(*numbers, **options):
    show_count = options.get("show_count", True)
    s = sum(numbers)
    return (s, len(numbers)) if show_count else s
print(summarize(1,2,3, show_count=False))
print(summarize(1,2,3,4,5))
