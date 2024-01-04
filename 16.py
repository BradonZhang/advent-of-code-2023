import itertools
from collections import deque

with open("16.txt") as f:
    grid = [list(x) for x in f.read().strip().splitlines()]

R = len(grid)
C = len(grid[0])
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

best = 0

UU = [((R, c), 0) for c in range(C)]
RR = [((r, -1), 1) for r in range(R)]
DD = [((-1, c), 2) for c in range(C)]
LL = [((r, C), 3) for r in range(R)]

for start in itertools.chain(RR, DD, LL, UU):
    seen = set()
    q = deque([start])
    while q:
        (r, c), d = q.popleft()
        dr, dc = D[d]
        r2, c2 = r + dr, c + dc
        if not (0 <= r2 < R) or not (0 <= c2 < C):
            continue
        x = grid[r2][c2]
        dd = []
        if x == "\\":
            dd.append([3, 2, 1, 0][d])
        elif x == "/":
            dd.append([1, 0, 3, 2][d])
        elif x == "|":
            if d in (0, 2):
                dd.append(d)
            else:
                dd.append(0)
                dd.append(2)
        elif x == "-":
            if d in (0, 2):
                dd.append(1)
                dd.append(3)
            else:
                dd.append(d)
        else:
            assert x == "."
            dd.append(d)
        for d2 in dd:
            key = ((r2, c2), d2)
            if key in seen:
                continue
            seen.add(key)
            q.append(key)

    cand = len(set(p for p, _ in seen))
    best = max(best, cand)
    if start == ((0, -1), 1):
        print(cand)

print(best)
