import sys
from collections import deque, defaultdict


sys.setrecursionlimit(100000)

with open("23.txt") as f:
    grid = [list(line) for line in f.read().strip().splitlines()]

R = len(grid)
C = len(grid[0])
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

start = (0, 1)
dest = (R - 1, C - 2)


def longest(r, c, seen=None):
    if (r, c) == dest:
        return len(seen)
    if not seen:
        seen = set()
    seen.add((r, c))
    best = 0
    for d, (dr, dc) in enumerate(D):
        r2 = r + dr
        c2 = c + dc
        if r2 < 0 or r2 >= R or c2 < 0 or c2 >= C:
            continue
        ch = grid[r2][c2]
        if ch == "#":
            continue
        if (r2, c2) in seen:
            continue
        if grid[r][c] in "^>v<" and "^>v<".index(grid[r][c]) != d:
            continue
        if grid[r2][c2] in "^>v<" and "v<^>".index(ch) == d:
            continue
        best = max(best, longest(r2, c2, seen))
    seen.discard((r, c))
    return best


print(longest(*start))


joints = {start, dest}

q = deque([start])
seen = {start}
while q:
    r, c = q.popleft()
    num_neighbors = 0
    for dr, dc in D:
        r2 = r + dr
        c2 = c + dc
        if r2 < 0 or r2 >= R or c2 < 0 or c2 >= C:
            continue
        if grid[r2][c2] == "#":
            continue
        num_neighbors += 1
        if (r2, c2) in seen:
            continue
        seen.add((r2, c2))
        q.append((r2, c2))
    if num_neighbors > 2:
        joints.add((r, c))


edges = defaultdict(lambda: defaultdict(lambda: 0))


def assign_edges(r, c, joint, w=0, seen=None):
    if seen is None:
        seen = set()
    seen.add((r, c))
    for dr, dc in D:
        r2 = r + dr
        c2 = c + dc
        if r2 < 0 or r2 >= R or c2 < 0 or c2 >= C:
            continue
        if grid[r2][c2] == "#":
            continue
        if (r2, c2) in seen:
            continue
        if (r2, c2) in joints:
            edges[joint][r2, c2] = max(w + 1, edges[joint][r2, c2])
        else:
            assign_edges(r2, c2, joint, w + 1, seen)
    seen.discard((r, c))


for joint in joints:
    assign_edges(*joint, joint)

for a in joints:
    for b in joints:
        if b in edges[a]:
            assert edges[a][b] == edges[b][a]
            assert edges[a][b] != -1
        else:
            assert a not in edges[b]


def longest(r, c, seen=None):
    if (r, c) == start:
        return 0
    if seen is None:
        seen = set()
    seen.add((r, c))
    best = None
    assert (r, c) in joints, (r, c)
    assert len(edges[r, c]) > 0
    for (r2, c2), w in edges[r, c].items():
        if (r2, c2) in seen:
            continue
        res = longest(r2, c2, seen)
        if res is None:
            continue
        if best is None:
            best = 0
        best = max(res + w, best)
    seen.discard((r, c))
    return best


print(longest(*dest))
