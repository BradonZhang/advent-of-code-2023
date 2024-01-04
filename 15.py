from collections import defaultdict, OrderedDict

with open("15.txt") as f:
    texts = f.read().strip().split(",")

p1 = 0
for text in texts:
    ans = 0
    for c in text:
        ans += ord(c)
        ans *= 17
        ans %= 256
    p1 += ans
print(p1)


p1 = 0
mem = defaultdict(OrderedDict)
for text in texts:
    label, val = text.replace("-", "=").split("=")
    box = 0
    for c in label:
        box += ord(c)
        box *= 17
        box %= 256
    if val == "":
        if label in mem[box]:
            mem[box].pop(label)
    else:
        mem[box][label] = int(val)

p2 = 0
for box, lenses in mem.items():
    for slot, foc in enumerate(lenses.values()):
        p2 += (box + 1) * (slot + 1) * foc
print(p2)
