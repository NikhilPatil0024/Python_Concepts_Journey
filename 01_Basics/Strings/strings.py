"""String basics: indexing, slicing, f-strings."""
text = "Python"
first = text[0]
last = text[-1]
slice_ = text[1:4]
msg = f"{text} has {len(text)} letters."
print(first, last, slice_, msg)
