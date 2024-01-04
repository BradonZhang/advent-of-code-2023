import math
from collections import deque

with open("20.txt") as f:
    lines = f.read().strip().splitlines()


modtypes = {}
dests = {}
state = {}
for line in lines:
    A, B = line.split(" -> ")
    if A == "broadcaster":
        module = A
        modtypes[module] = A
    else:
        module = A[1:]
        modtypes[module] = A[0]
    destlist = B.split(", ")
    dests[module] = destlist
    if modtypes[module] == "&":
        state[module] = {}
    else:
        state[module] = 0

gatekeepers = set()
grand_gatekeeper = None
for module in dests:
    for dest in dests[module]:
        if dest == "rx":
            grand_gatekeeper = module
        if modtypes.get(dest) == "&":
            state[dest][module] = 0
for module in dests:
    for dest in dests[module]:
        if dest == grand_gatekeeper:
            gatekeepers.add(module)

q = deque()
sig_counts = [0, 0]
for i in range(1000):
    q.append(("button", "broadcaster", 0))
    while q:
        source, module, sig = q.popleft()
        sig_counts[sig] += 1
        if module not in modtypes and sig == 1:
            continue
        if modtypes[module] == "%":
            if sig == 1:
                continue
            state[module] = 1 - state[module]
            for dest in dests[module]:
                q.append((module, dest, state[module]))
        elif modtypes[module] == "&":
            state[module][source] = sig
            for dest in dests[module]:
                q.append((module, dest, 1 - all(state[module].values())))
        else:
            assert module == "broadcaster", module
            for dest in dests[module]:
                q.append((module, dest, state[module]))
    if any(state["dt"].values()):
        print(i + 1, state["dt"])

print(sig_counts[0] * sig_counts[1])


systems = {}
for start in dests["broadcaster"]:
    seen = {start}
    q = deque(seen)
    while q:
        curr = q.popleft()
        for dest in dests[curr]:
            if dest in seen:
                continue
            if dest in gatekeepers:
                continue
            seen.add(dest)
            q.append(dest)
    systems[start] = seen
assert all(
    x == y or len(x & y) == 0 for x in systems.values() for y in systems.values()
)


def freeze_state(state):
    res = frozenset()
    for module, value in state.items():
        if isinstance(value, dict):
            value = frozenset(value.items())
        res |= frozenset({(module, value)})
    return res


p2 = 1
for start, system in systems.items():
    assert sum(modtypes[module] == '&' for module in system) == 1
    state = {}
    for module in system:
        if modtypes[module] == "&":
            state[module] = {}
        else:
            state[module] = 0
    for module in system:
        for dest in dests[module]:
            if dest not in system:
                continue
            if modtypes.get(dest) == "&":
                state[dest][module] = 0

    t = 0
    states = {freeze_state(state): 0}
    passes = []
    while True:
        t += 1
        q = deque([("broadcaster", start, 0)])
        while q:
            source, module, sig = q.popleft()
            if module not in system:
                continue
            if modtypes[module] == "%":
                if sig == 1:
                    continue
                state[module] = 1 - state[module]
                for dest in dests[module]:
                    q.append((module, dest, state[module]))
            elif modtypes[module] == "&":
                state[module][source] = sig
                all_high = all(state[module].values())
                for dest in dests[module]:
                    q.append((module, dest, 1 - all_high))
                if all_high:
                    passes.append(t)
            else:
                raise RuntimeError
        fs = freeze_state(state)
        if fs in states:
            break
        states[t] = fs
    assert states[fs] == 0
    assert passes == [len(states)]
    p2 = math.lcm(p2, len(states))


print(p2)
