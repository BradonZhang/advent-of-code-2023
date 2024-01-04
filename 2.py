import math
import re

with open("2.txt") as f:
    lines = f.read().strip().splitlines()

ans = 0
for line in lines:
    storage = {"red": 12, "green": 13, "blue": 14}
    game_id, *counts = map(int, re.findall(r"\d+", line))
    colors = re.findall(r"red|green|blue|;", line)
    color_iter = iter(colors)
    for count in counts:
        color = next(color_iter)
        if color == ";":
            storage = {"red": 12, "green": 13, "blue": 14}
            color = next(color_iter)
        storage[color] -= count
        if storage[color] < 0:
            break
    else:
        ans += game_id

print(ans)

ans = 0
for line in lines:
    required = {"red": 0, "green": 0, "blue": 0}
    storage = {"red": 0, "green": 0, "blue": 0}
    game_id, *counts = map(int, re.findall(r"\d+", line))
    colors = re.findall(r"red|green|blue|;", line)
    color_iter = iter(colors)
    for count in counts:
        color = next(color_iter)
        if color == ";":
            storage = {"red": 0, "green": 0, "blue": 0}
            color = next(color_iter)
        storage[color] += count
        required[color] = max(required[color], storage[color])
    ans += math.prod(required.values())

print(ans)
