import random
# from collections import defaultdict
# from dataclasses import dataclass


# @dataclass
# class Edge:
#     a: set[str]
#     b: set[str]

#     @property
#     def is_valid(self):
#         return len(a) > 0 and len(b) > 0 and len(a & b) == 0 and min(a) < min(b)


# @dataclass
# class WeightedEdge(Edge):
#     weight: int


with open("25.txt") as f:
    lines = f.read().strip().splitlines()


# edges: list[Edge] = []
# for line in lines:
#     source, *parts = line.replace(':', '').split()
#     for part in parts:
#         a = {min(source, part)}
#         b = {max(source, part)}
#         edges.append(Edge(a, b))

# print(edges)
# exit()

# wirings = defaultdict(set)
edges: set[frozenset[frozenset[str]]] = set()
for line in lines:
    source, *parts = line.replace(':', '').split()
    # print(source, '--', ', '.join(parts))
    for part in parts:
        # wirings[source].add(part)
        # wirings[part].add(source)
        n1 = frozenset({part})
        n2 = frozenset({source})
        edges.add(frozenset({n1, n2}))

cut = None
num_tries = 0
while cut != 3:
    num_tries += 1
    temp_edges = set(edges)
    while len(temp_edges) > 1:
        # print()
        # print(edges)
        x = random.choice(tuple(temp_edges))
        a, b = tuple(x)
        assert len(a & b) == 0
        node = a | b
        new_edges = set()
        for edge in temp_edges:
            if edge == x:
                continue
            new_edge = edge
            if a in edge:
                new_edge -= frozenset({a})
                new_edge |= frozenset({node})
            if b in edge:
                new_edge -= frozenset({b})
                new_edge |= frozenset({node})
            new_edges.add(new_edge)
        temp_edges = new_edges
    assert len(temp_edges) == 1
    A, B = next(iter(temp_edges))
    cut = 0
    for edge in edges:
        a, b = tuple(edge)
        a = next(iter(a))
        b = next(iter(b))
        if (a in A and b in B) or (a in B and b in A):
            cut += 1

a, b = tuple(temp_edges)[0]
print(len(a) * len(b))
