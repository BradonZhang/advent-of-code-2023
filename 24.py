import re
from dataclasses import dataclass
from fractions import Fraction

import sympy

with open("24.txt") as f:
    lines = f.read().strip().splitlines()


@dataclass
class Hail:
    px: int
    py: int
    pz: int
    vx: int
    vy: int
    vz: int

    @property
    def m(self):
        return Fraction(self.vy, self.vx)

    @property
    def y0(self):
        return self.py - self.m * self.px

    def f(self, x):
        return self.m * x + self.y0

    def test(self, minx, maxx, miny, maxy):
        if miny <= self.f(minx) <= maxy or miny <= self.f(maxx) <= maxy:
            return True
        if self.f(minx) < miny:
            return self.f(maxx) >= miny
        else:
            assert self.f(minx) > maxy
        return self.f(maxx) <= maxy

    def time(self, x, y):
        tx = Fraction(x - self.px, self.vx)
        ty = Fraction(y - self.py, self.vy)
        assert tx == ty
        return tx

    def ft(self, t):
        return (self.px + t * self.vx, self.py + t * self.vy, self.pz + t * self.vz)


hails: list[Hail] = []
for line in lines:
    px, py, pz, vx, vy, vz = map(int, re.findall(r"-?\d+", line))
    assert vx and vy and vz
    hails.append(Hail(px, py, pz, vx, vy, vz))

L = 200000000000000
U = 400000000000000

# total = 0
# for i in range(len(hails)):
#     for j in range(i + 1, len(hails)):
#         h1 = hails[i]
#         h2 = hails[j]
#         if h1.m == h2.m:
#             total += h1.y0 == h2.y0 and h1.test(L, U, L, U)
#             continue
#         x = Fraction(h2.y0 - h1.y0, h1.m - h2.m)
#         y = h1.f(x)
#         if h1.time(x, y) < 0 or h2.time(x, y) < 0:
#             continue
#         assert y == h2.f(x), (x, y, h1.f(x), h2.f(x))
#         if L <= x <= U and L <= y <= U:
#             total += 1

# print(total)


px, py, pz, vx, vy, vz = sympy.symbols('px py pz vx vy vz', integer=True)
T = sympy.symbols(f't:{len(hails)}', integer=True)
eqs: list[sympy.Eq] = []


# We only need the first three hailstones - 9 equations for 9 variables
for hail, t in list(zip(hails, T))[:3]:
    eqs.append(sympy.Eq(hail.px - px, t * (vx - hail.vx)))
    eqs.append(sympy.Eq(hail.py - py, t * (vy - hail.vy)))
    eqs.append(sympy.Eq(hail.pz - pz, t * (vz - hail.vz)))

res = sympy.solve(eqs)[0]
print(res[px] + res[py] + res[pz])
