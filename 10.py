from collections import deque

with open("10.txt") as f:
    grid = f.read().strip().splitlines()

M = len(grid)
N = len(grid[0])
for i, line in enumerate(grid):
    for j, x in enumerate(line):
        if x == 'S':
            break
    else:
        continue
    break

S = (i, j)
dists = {S: 0}

q = deque([S])
D = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(0, 1), (-1, 0)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)],
    'S': [(-1, 0), (0, -1), (0, 1), (1, 0)],
    '.': [],
}
while q:
    r, c = q.popleft()
    x = grid[r][c]
    for dr, dc in D[x]:
        r2, c2 = r + dr, c + dc
        if not (0 <= r2 < M) or not (0 <= c2 < N):
            continue
        if (r2, c2) in dists:
            continue
        if (-dr, -dc) not in D[grid[r2][c2]]:
            continue
        dists[r2, c2] = dists[r, c] + 1
        q.append((r2, c2))
    if x == 'S':
        s_neighbors = set((r - S[0], c - S[1]) for (r, c) in q)
        for label, identity in D.items():
            if set(identity) == s_neighbors:
                s_identity = label

print(max(dists.values()))


OO = min(dists)
curr = (OO[0], OO[1] + 1)
faces = [(0, 1), (1, 0), (0, -1), (-1, 0)]
face = (0, 1)
border = set()
assert grid[OO[0]][OO[1]] in 'FS'
assert curr in dists
while curr != OO:
    r, c = curr
    x = grid[r][c]
    if x == 'S':
        x = s_identity
    candidates = []
    right = faces[(faces.index(face) + 1) % 4]
    left = (-right[0], -right[1])
    back = (-face[0], -face[1])
    if x in '|-':
        candidates.append(right)
    elif x in '7FJL':
        rf, cf = face
        # left turn
        if D[x].index(back) == 1:
            candidates.append(face)
            candidates.append(right)
            face = left
        # right turn
        else:
            face = right
    for dr, dc in candidates:
        r2, c2 = r + dr, c + dc
        if (r2, c2) in dists:
            continue
        border.add((r2, c2))
    curr = (curr[0] + face[0], curr[1] + face[1])

inside = set()
for start in border:
    if start in inside:
        continue
    q = deque([start])
    inside.add(start)
    while q:
        r, c = q.popleft()
        for dr, dc in faces:
            r2, c2 = r + dr, c + dc
            if not (0 <= r2 < M) or not (0 <= c2 < N):
                continue
            if (r2, c2) in dists:
                continue
            if (r2, c2) in inside:
                continue
            assert (r2, c2) not in inside
            inside.add((r2, c2))
            q.append((r2, c2))
print(len(inside))
