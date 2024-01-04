from collections import deque

with open("21.txt") as f:
    G = [list(line) for line in f.read().strip().splitlines()]

R = len(G)
C = len(G[0])
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

S = None
for i, line in enumerate(G):
    if "S" in line:
        S = (i, line.index("S"))

seen = {S: 0}
q = deque([S])
while q:
    r, c = q.popleft()
    for dr, dc in D:
        r2, c2 = r + dr, c + dc
        if not (0 <= r2 < R) or not (0 <= c2 < C):
            continue
        if G[r2][c2] == "#":
            continue
        if (r2, c2) in seen:
            continue
        seen[r2, c2] = seen[r, c] + 1
        q.append((r2, c2))

print(sum(x <= 64 and x % 2 == 0 for x in seen.values()))


T = 26501365
assert R == C
assert R % 2 == 1
assert T % R == R // 2
assert all(
    (r, c) in seen
    for r in range(R)
    for c in range(C)
    if r in (0, R - 1) or c in (0, C - 1)
)
length = T // R
med = T % R

full = [0, 0]
corners = [0, 0]
for (r, c), dist in seen.items():
    p = dist % 2
    full[p] += 1
    if r + c < med or c - r > med or r - c > med or r + c > med * 3:
        corners[p] += 1

print(
    # Odd full grids
    (length + 1) ** 2 * full[1]
    # Even full grids
    + length**2 * full[0]
    # Odd corner parts
    - (length + 1) * corners[1]
    # Even corner parts
    + length * corners[0]
)
