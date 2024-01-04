import re
import itertools
import math

with open("8.txt") as f:
    ins, routes_text = f.read().strip().split('\n\n')

routes = {}
for route in routes_text.splitlines():
    a, b, c = re.findall(r'[A-Z]{3}', route)
    routes[a] = (b, c)

curr = 'AAA'
total = 0
for x in itertools.cycle(ins):
    total += 1
    curr = routes[curr][x == 'R']
    if curr == 'ZZZ':
        break

print(total)


mults = []
for curr in routes:
    if not curr.endswith('A'):
        continue
    mults.append(0)
    for x in itertools.cycle(ins):
        mults[-1] += 1
        curr = routes[curr][x == 'R']
        if curr.endswith('Z'):
            break

print(math.lcm(*mults))
