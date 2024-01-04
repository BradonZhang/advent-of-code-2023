from copy import deepcopy

with open("14.txt") as f:
    G = [list(line) for line in f.read().strip().splitlines()]

R = len(G)
C = len(G[0])

total = 0
for c in range(C):
    platform = -1
    streak = 0
    for r in range(R):
        x = G[r][c]
        if x == "#":
            streak = 0
            platform = r
        elif x == "O":
            streak += 1
            total += R - (platform + streak)
print(total)


def merge(G):
    return "".join("".join(line) for line in G)


def score(G):
    return sum((R - r) * (line.count("O")) for r, line in enumerate(G))


count = 0
seen = {merge(G): 0}
scores = [score(G)]
T = 10**9
for t in range(T):
    G_ = deepcopy(G)
    for c in range(C):
        platform = -1
        for r in range(R):
            x = G_[r][c]
            if x == "#":
                platform = r
            elif x == "O":
                platform += 1
                G_[r][c] = "."
                G_[platform][c] = "O"
    for r in range(R):
        platform = -1
        for c in range(C):
            x = G_[r][c]
            if x == "#":
                platform = c
            elif x == "O":
                platform += 1
                G_[r][c] = "."
                G_[r][platform] = "O"
    for c in range(C):
        platform = R
        for r in range(R - 1, -1, -1):
            x = G_[r][c]
            if x == "#":
                platform = r
            elif x == "O":
                platform -= 1
                G_[r][c] = "."
                G_[platform][c] = "O"
    for r in range(R):
        platform = C
        for c in range(C - 1, -1, -1):
            x = G_[r][c]
            if x == "#":
                platform = c
            elif x == "O":
                platform -= 1
                G_[r][c] = "."
                G_[r][platform] = "O"
    G = G_
    G__ = merge(G)
    if G__ in seen:
        break
    seen[G__] = t + 1
    scores.append(score(G))
else:
    print(scores[-1])
    exit()

start = seen[G__]
period = t + 1 - start
print(scores[start + (T - start) % period])
