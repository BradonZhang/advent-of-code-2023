import math
import re

with open("3.txt") as f:
    text = f.read().strip()
    grid = text.splitlines()

M = len(grid)
N = len(grid[0])

total = 0
for i, line in enumerate(grid):
    for m in re.finditer(r'\d+', line):
        for j in range(*m.span()):
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    i2 = i + di
                    j2 = j + dj
                    if (0 <= i2 < M) and (0 <= j2 < N):
                        c = grid[i2][j2]
                        if not re.match(r'\d|\.', c):
                            total += int(m.group(0))
                            break
                else:
                    continue
                break
            else:
                continue
            break
print(total)


total = 0
for i, line in enumerate(grid):
    for j, x in enumerate(line):
        if x != '*':
            continue

        def make_num(i, j):
            if not (0 <= i < M) or not (0 <= j < N):
                return None
            num_str = grid[i][j]
            if not ('0' <= num_str <= '9'):
                return None
            for j2 in range(j - 1, -1, -1):
                if not ('0' <= grid[i][j2] <= '9'):
                    break
                num_str = grid[i][j2] + num_str
            for j2 in range(j + 1, N):
                if not ('0' <= grid[i][j2] <= '9'):
                    break
                num_str = num_str + grid[i][j2]
            return int(num_str)

        raw_nums = [make_num(i + di, j + dj) for di in range(-1, 2) for dj in range(-1, 2)]
        nums = []
        if (x := raw_nums[1]) is not None:
            nums.append(x)
        else:
            if (x := raw_nums[0]) is not None:
                nums.append(x)
            if (x := raw_nums[2]) is not None:
                nums.append(x)
        if (x := raw_nums[3]) is not None:
            nums.append(x)
        if (x := raw_nums[5]) is not None:
            nums.append(x)
        if (x := raw_nums[7]) is not None:
            nums.append(x)
        else:
            if (x := raw_nums[6]) is not None:
                nums.append(x)
            if (x := raw_nums[8]) is not None:
                nums.append(x)
        if len(nums) == 2:
            total += math.prod(nums)
        continue

print(total)
