"""Nested conditions with elif."""
n = -3
if n > 0:
    print("positive")
elif n == 0:
    print("zero")
else:
    if n % 2 == 0:
        print("negative even")
    else:
        print("negative odd")
