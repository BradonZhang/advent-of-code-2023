from collections import defaultdict

with open("4.txt") as f:
    lines = f.read().strip().splitlines()

p1 = 0
p2 = 0
num_copies = defaultdict(lambda: 1)
for i, line in enumerate(lines):
    winning, have = line.split(':')[1].split('|')
    W = set(map(int, winning.split()))
    H = set(map(int, have.split()))
    p1 += int(2**(len(W & H) - 1))
    for j in range(len(W & H)):
        num_copies[i + 1 + j] += num_copies[i]
    p2 += num_copies[i]
print(p1)
print(p2)
