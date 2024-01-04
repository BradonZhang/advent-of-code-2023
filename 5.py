with open("5.txt") as f:
    seeds, *conversions = f.read().strip().split('\n\n')
    seeds = list(map(int, seeds.split(': ')[1].split()))
    conversions = [[tuple(map(int, line.split())) for line in conversion.splitlines()[1:]] for conversion in conversions]

best_value = float('inf')
for seed in seeds:
    value = seed
    for conversion_chunk in conversions:
        for (a, b, c) in conversion_chunk:
            if b <= value < b + c:
                value += a - b
                break
    best_value = min(best_value, value)

print(best_value)


best_value = float('inf')
for seed0, seedn in zip(seeds[::2], seeds[1::2]):
    values = [(seed0, seedn)]
    for conversion_chunk in conversions:
        new_values = []
        while values:
            seed0, seedn = values.pop()
            for (a, b, c) in conversion_chunk:
                if seed0 < b < b + c < seed0 + seedn:
                    values.append((seed0, b - seed0))
                    values.append((b + c, seed0 + seedn - b - c))
                    new_values.append((a, c))
                    break
                elif b <= seed0 < seed0 + seedn <= b + c:
                    new_values.append((seed0 + a - b, seedn))
                    break
                elif b <= seed0 < b + c < seed0 + seedn:
                    values.append((b + c, seed0 + seedn - b - c))
                    new_values.append((seed0 + a - b, b + c - seed0))
                    break
                elif seed0 < b < seed0 + seedn <= b + c:
                    values.append((seed0, b - seed0))
                    new_values.append((a, seed0 + seedn - b))
                    break
            else:
                new_values.append((seed0, seedn))
        values = new_values
    best_value = min(best_value, min(x[0] for x in values))

print(best_value)
