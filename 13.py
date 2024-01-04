from copy import deepcopy

with open("13.txt") as f:
    chunks = [
        [list(line) for line in chunk.splitlines()]
        for chunk in f.read().strip().split("\n\n")
    ]

def get_lor(G, exclude=None):
    for i in range(1, len(G)):
        if i == exclude:
            continue
        x = G[:i][::-1]
        y = G[i:]
        ln = min(len(x), len(y))
        if x[:ln] == y[:ln]:
            return i
    return None

p1 = 0
p2 = 0
for rows in chunks:
    columns = [list(x) for x in zip(*rows)]
    assert [list(x) for x in zip(*columns)] == rows
    rline = False
    if (lor := get_lor(rows)):
        p1 += 100 * lor
        rline = True
    elif (lor := get_lor(columns)):
        p1 += lor
    else:
        assert False
    for r in range(len(rows)):
        for c in range(len(columns)):
            rows_ = deepcopy(rows)
            columns_ = deepcopy(columns)
            rows_[r][c] = '#' if rows[r][c] == '.' else '.'
            columns_[c][r] = '#' if columns[c][r] == '.' else '.'
            if (lor_ := get_lor(rows_, lor if rline else None)):
                p2 += 100 * lor_
                break
            elif (lor_ := get_lor(columns_, None if rline else lor)):
                p2 += lor_
                break
        else:
            continue
        break


print(p1)
print(p2)

exit()

# Old solution
p1 = 0
p2 = 0
for chunk in chunks:
    chunk = [''.join(row) for row in chunk]
    R = len(chunk)
    C = len(chunk[0])

    hlor = None
    vlor = None
    for i in range(1, R):
        x = chunk[:i][::-1]
        y = chunk[i:]
        ln = min(len(x), len(y))
        if x[:ln] == y[:ln]:
            p1 += i * 100
            hlor = i
            break
    for i in range(1, C):
        x = ["".join(line[j] for line in chunk) for j in range(i)][::-1]
        y = ["".join(line[j] for line in chunk) for j in range(i, C)]
        ln = min(len(x), len(y))
        if x[:ln] == y[:ln]:
            p1 += i
            vlor = i
            break

    chunk_base = "\n".join(chunk)
    added = False
    for t in range(len(chunk_base)):
        if chunk_base[t] == "\n":
            continue
        new_char = "#" if chunk_base[t] == "." else "."
        chunk_text = chunk_base[:t] + new_char + chunk_base[t + 1 :]
        assert len(chunk_text) == len(chunk_base)
        chunk = chunk_text.splitlines()
        for i in range(1, R):
            if i == hlor:
                continue
            x = chunk[:i][::-1]
            y = chunk[i:]
            ln = min(len(x), len(y))
            assert ln
            if x[:ln] == y[:ln]:
                p2 += i * 100
                added = True
                break
        for i in range(1, C):
            if i == vlor:
                continue
            x = ["".join(line[j] for line in chunk) for j in range(i)][::-1]
            y = ["".join(line[j] for line in chunk) for j in range(i, C)]
            ln = min(len(x), len(y))
            assert ln
            if x[:ln] == y[:ln]:
                p2 += i
                added = True
                break
        if added:
            break
    assert added

print(p1)
print(p2)
