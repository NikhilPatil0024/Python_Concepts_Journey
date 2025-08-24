"""Nested loops for a simple multiplication table (1..3)."""
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i*j)
    print(row)
