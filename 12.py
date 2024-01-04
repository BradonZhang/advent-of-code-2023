import re
import functools

with open("12.txt") as f:
    lines = f.read().strip().splitlines()

@functools.lru_cache(maxsize=None)
def dp(row, counts):
    if not counts:
        return int('#' not in row)
    if not row:
        return 0
    total = 0
    if not row.startswith('#'):
        total += dp(row[1:], counts)
    if re.match(fr'^[#\?]{{{counts[0]}}}(?!#)', row):
        total += dp(row[counts[0] + 1:], counts[1:])
    return total

p1 = 0
p2 = 0
for line in lines:
    row, counts = line.split()
    counts = tuple(map(int, counts.split(',')))
    p1 += dp(row, counts)
    p2 += dp('?'.join([row] * 5), counts * 5)
print(p1)
print(p2)
