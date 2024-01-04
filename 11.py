with open("11.txt") as f:
    lines = f.read().strip().splitlines()

M = len(lines)
N = len(lines[0])

galaxies = []
empty_rows = []
empty_cols = []

for i, line in enumerate(lines):
    if not any(x == '#' for x in line):
        empty_rows.append(i)
    for j, x in enumerate(line):
        if line[j] == '#':
            galaxies.append((i, j))
for j in range(N):
    if not any(line[j] == '#' for line in lines):
        empty_cols.append(j)

p1 = 0
p2 = 0
for i, (r1, c1) in enumerate(galaxies):
    for j, (r2, c2) in enumerate(galaxies):
        if j <= i:
            continue
        dist = abs(r2 - r1) + abs(c2 - c1)
        dr = sum(min(r1, r2) < r < max(r1, r2) for r in empty_rows)
        dc = sum(min(c1, c2) < c < max(c1, c2) for c in empty_cols)
        p1 += dist + dr + dc
        p2 += dist + (dr + dc) * 999999

print(p1)
print(p2)
