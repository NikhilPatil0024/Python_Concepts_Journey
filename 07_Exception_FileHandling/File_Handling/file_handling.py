"""Safely reading and writing files with context managers."""
path = "sample.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write("hello\nworld\n")
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
