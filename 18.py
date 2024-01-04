from collections import deque

with open("18.txt") as f:
    lines = f.read().strip().splitlines()

D = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}
posr, posc = (0, 0)
edge = {(posr, posc)}
for line in lines:
    d, num, _ = line.split()
    num = int(num)
    dr, dc = D[d]
    assert dr != dc and dr * dc == 0
    for i in range(num):
        posr += dr
        posc += dc
        edge.add((posr, posc))

minx = min(x[0] for x in edge)
maxx = max(x[0] for x in edge)
miny = min(x[1] for x in edge)
maxy = max(x[1] for x in edge)

regions = [edge]
for x in range(minx, maxx + 1):
    for y in range(miny, maxy + 1):
        if any((x, y) in region for region in regions):
            continue
        q = deque([(x, y)])
        regions.append(set())
        while q:
            r, c = q.pop()
            for dr, dc in D.values():
                r2 = dr + r
                c2 = dc + c
                if (r2, c2) in edge or (r2, c2) in regions[-1]:
                    continue
                if not (minx <= r2 <= maxx) or not (miny <= c2 <= maxy):
                    continue
                regions[-1].add((r2, c2))
                q.append((r2, c2))

print(len(edge) + max(len(x) for x in regions[1:]))


# Improved part 1
# D = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# points = [(0, 0)]
# for line in lines:
#     d, num, _ = line.split()
#     num = int(num)
#     x, y = points[-1]
#     dx, dy = D['RDLU'.index(d)]
#     points.append((x + dx * num, y + dy * num))
# area = 0
# edge = 0
# for (x1, y1), (x2, y2) in zip(points[1:], points[:-1]):
#     area += x1 * y2 - x2 * y1
#     edge += abs(y2 - y1) + abs(x2 - x1)
# area = (abs(area) + edge) // 2 + 1
# print(area)


D = [(1, 0), (0, -1), (-1, 0), (0, 1)]
points = [(0, 0)]
for line in lines:
    code = line.split()[-1]
    num, d = int(code[2:-2], 16), int(code[-2])
    x, y = points[-1]
    dx, dy = D[d]
    points.append((x + dx * num, y + dy * num))
area = 0
edge = 0
for (x1, y1), (x2, y2) in zip(points[1:], points[:-1]):
    area += x1 * y2 - x2 * y1
    edge += abs(y2 - y1) + abs(x2 - x1)
area = (abs(area) + edge) // 2 + 1
print(area)
