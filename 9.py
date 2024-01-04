with open("9.txt") as f:
    lines = f.read().strip().splitlines()

p1 = 0
p2 = 0
for line in lines:
    pyramid = [list(map(int, line.split()))]
    while any(pyramid[-1]):
        level = []
        for i in range(len(pyramid[-1]) - 1):
            level.append(pyramid[-1][i + 1] - pyramid[-1][i])
        pyramid.append(level)
    p1 += sum(level[-1] for level in pyramid)
    p2 += sum(level[0] * (-1 if i % 2 else 1) for i, level in enumerate(pyramid))
print(p1)
print(p2)
