from collections import defaultdict, deque
from dataclasses import dataclass

with open("22.txt") as f:
    lines = f.read().strip().splitlines()


@dataclass
class Cube:
    id: int
    x: int
    y: int
    z: int
    length: int
    width: int
    height: int

    def __hash__(self) -> int:
        return self.id


cubes: list[Cube] = []
for i, line in enumerate(lines):
    a, b = line.split("~")
    x1, y1, z1 = map(int, a.split(","))
    x2, y2, z2 = map(int, b.split(","))
    assert x1 <= x2 and y1 <= y2 and z1 <= z2
    cubes.append(Cube(i, x1, y1, z1, x2 - x1 + 1, y2 - y1 + 1, z2 - z1 + 1))
cubes.sort(key=lambda cube: cube.z)

supported_by = defaultdict(set)
supports = defaultdict(set)
for i, cube1 in enumerate(cubes):
    z = None
    for cube2 in sorted(cubes[:i], key=lambda cube: cube.z + cube.height, reverse=True):
        if z is not None and cube2.z + cube2.height < z:
            break
        if (
            cube1.x <= cube2.x < cube1.x + cube1.length
            or cube2.x <= cube1.x < cube2.x + cube2.length
        ) and (
            cube1.y <= cube2.y < cube1.y + cube1.width
            or cube2.y <= cube1.y < cube2.y + cube2.width
        ):
            cube1.z = cube2.z + cube2.height
            z = cube1.z
            supported_by[cube2].add(cube1)
            supports[cube1].add(cube2)
    if z is None:
        cube1.z = 1


orphan_cubes = set(cubes)

for C in supports.values():
    if len(C) == 1:
        orphan_cubes.discard(next(iter(C)))
print(len(orphan_cubes))


p2 = 0
for cube in cubes:
    removed = {cube}
    q = deque(removed)
    while q:
        curr = q.popleft()
        for child in supported_by[curr] - removed:
            if len(supports[child] - removed) == 0:
                q.append(child)
                removed.add(child)
    p2 += len(removed) - 1

print(p2)
