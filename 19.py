import math
import re

with open("19.txt") as f:
    A, B = f.read().strip().split("\n\n")
    workflows_text = A.splitlines()
    parts = B.splitlines()


class Workflow:
    def __init__(self, line):
        self.name, rules_text, self.default = re.fullmatch(
            r"(\w+)\{((?:[xmas][<>]\d+\:\w+\,)+)(\w+)\}", line
        ).groups()
        self.rules = []
        for rule_text in rules_text.split(","):
            if not rule_text:
                continue
            self.rules.append(
                re.fullmatch(r"([xmas])([<>])(\d+)\:(\w+)", rule_text).groups()
            )

    def validate(self, part: dict) -> bool:
        for rule in self.rules:
            v, op, num, res = rule

            def op_(a, b):
                return a < b if op == "<" else a > b

            if op_(part[v], int(num)):
                if res in ["A", "R"]:
                    return res == "A"
                return workflows[res].validate(part)
        if self.default in ["A", "R"]:
            return self.default == "A"
        return workflows[self.default].validate(part)

    def count_range(self, restrictions: dict[str, tuple[int, int]]):
        total = 0
        r = dict(restrictions)
        for rule in self.rules:
            r2 = dict(r)
            v, op, num, res = rule
            num = int(num)
            a, b = r[v]
            tautology = False
            if op == ">":
                if num >= b:
                    continue
                elif num >= a:
                    r[v] = (a, num)
                    r2[v] = (num + 1, b)
                else:
                    tautology = True
            else:
                assert op == "<"
                if num <= a:
                    continue
                elif num <= b:
                    r[v] = (num, b)
                    r2[v] = (a, num - 1)
                else:
                    tautology = True
            if res == "A":
                total += math.prod((b - a + 1) for a, b in r2.values())
            elif res != "R":
                total += workflows[res].count_range(r2)
            else:
                assert res == "R"
            if tautology:
                return total
        if self.default == "A":
            total += math.prod((b - a + 1) for a, b in r.values())
        elif self.default != "R":
            total += workflows[self.default].count_range(r)
        else:
            assert self.default == "R"
        return total


workflows = {line.split("{")[0]: Workflow(line) for line in workflows_text}

total = 0
for part_text in parts:
    part = eval(f"dict({part_text[1:-1]})")
    if workflows["in"].validate(part):
        total += sum(part.values())
print(total)

print(workflows["in"].count_range({v: (1, 4000) for v in "xmas"}))
