with open("6.txt") as f:
    tline, dline = f.read().strip().splitlines()
    times = list(map(int, tline.split()[1:]))
    dists = list(map(int, dline.split()[1:]))

product = 1
for t, d in zip(times, dists):
    total = 0
    for i in range(t + 1):
        total += i * (t - i) > d
    product *= total

print(product)


T = int(''.join(map(str, times)))
D = int(''.join(map(str, dists)))
tmin = 0
tmax = T // 2
while tmax > tmin:
    tmed = (tmax + tmin) // 2 + 1
    if tmed * (T - tmed) > D:
        tmax = tmed - 1
    else:
        tmin = tmed
assert tmin == tmax
t0 = tmin

tmin = T // 2 + 1
tmax = T
while tmax > tmin:
    tmed = (tmax + tmin) // 2
    if tmed * (T - tmed) > D:
        tmin = tmed + 1
    else:
        tmax = tmed
assert tmin == tmax

print(tmax - t0 - 1)


# # Direct answer

# import math

# a = 1
# b = -T
# c = D
# print(math.floor((T**2 - 4 * D)**0.5 / 2) - math.ceil(-(T**2 - 4 * D)**0.5 / 2) + 1)
