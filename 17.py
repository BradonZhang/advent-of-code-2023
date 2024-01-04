import heapq

with open("17.txt") as f:
    grid = [[int(x) for x in line] for line in f.read().strip().splitlines()]


R = len(grid)
C = len(grid[0])
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pq = [(0, 0, 0, 1, 3), (0, 0, 0, 2, 3)]
best = {}
while pq:
    h, r, c, d, rem = heapq.heappop(pq)
    if h >= best.get((r, c, d, rem), float("inf")):
        continue
    best[r, c, d, rem] = h
    cands = []
    if rem:
        dr, dc = D[d]
        cands.append((r + dr, c + dc, d, rem - 1))
    for d2 in [(d - 1) % 4, (d + 1) % 4]:
        dr, dc = D[d2]
        cands.append((r + dr, c + dc, d2, 2))
    for cand in cands:
        r2, c2, d2, rem2 = cand
        if not (0 <= r2 < R) or not (0 <= c2 < C):
            continue
        h2 = h + grid[r2][c2]
        heapq.heappush(pq, (h2, *cand))

bestie = float("inf")
for (r, c, d, rem), h in best.items():
    if (r, c) == (R - 1, C - 1):
        bestie = min(h, bestie)
print(bestie)


pq = [(0, 0, 0, 1, 10), (0, 0, 0, 2, 10)]
best = {}
while pq:
    h, r, c, d, rem = heapq.heappop(pq)
    if h >= best.get((r, c, d, rem), float("inf")):
        continue
    best[r, c, d, rem] = h
    cands = []
    if rem:
        dr, dc = D[d]
        cands.append((r + dr, c + dc, d, rem - 1))
    if rem <= 6:
        for d2 in [(d - 1) % 4, (d + 1) % 4]:
            dr, dc = D[d2]
            cands.append((r + dr, c + dc, d2, 9))
    for cand in cands:
        r2, c2, d2, rem2 = cand
        if not (0 <= r2 < R) or not (0 <= c2 < C):
            continue
        h2 = h + grid[r2][c2]
        heapq.heappush(pq, (h2, *cand))


bestie = float("inf")
for (r, c, d, rem), h in best.items():
    if (r, c) == (R - 1, C - 1):
        bestie = min(h, bestie)
print(bestie)
