import re

with open("1.txt") as f:
    lines = f.read().strip().splitlines()

p1 = 0
p2 = 0
for line in lines:
    nums = re.findall(r'\d', line)
    p1 += int(nums[0] + nums[-1])
    first = None
    last = None
    num = 0
    for x in re.finditer(
        r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))", line
    ):
        x = x.group(1)
        if "0" <= x <= "9":
            x = int(x)
        else:
            x = [
                "zero",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ].index(x)
        if first is None:
            first = x
            num += first * 10
        last = x
    if last is not None:
        num += last
    p2 += num

print(p1)
print(p2)
