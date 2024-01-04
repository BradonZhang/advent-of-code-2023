import itertools
from collections import Counter
from dataclasses import dataclass


@dataclass
class Hand:
    cards: str
    bid: int

    @property
    def handtype(self):
        c = Counter(self.cards).most_common()
        if c[0][1] == 5:
            return 6
        if c[0][1] == 4:
            return 5
        if c[0][1] == 3 and c[1][1] == 2:
            return 4
        if c[0][1] == 3:
            return 3
        if c[0][1] == 2 and c[1][1] == 2:
            return 2
        if c[0][1] == 2:
            return 1
        return 0

    @property
    def highcards(self):
        faces = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10,
        }
        return tuple(int(faces.get(card, card)) for card in self.cards)


with open("7.txt") as f:
    lines = f.read().strip().splitlines()

hands: list[Hand] = []
for line in lines:
    cards, bid = line.split()
    hands.append(Hand(cards, int(bid)))

hands.sort(key=lambda hand: (hand.handtype, hand.highcards))
print(sum((i + 1) * hand.bid for i, hand in enumerate(hands)))


@dataclass
class Hand:
    cards: str
    bid: int

    @property
    def handtype(self):
        options = [str(x) for x in range(2, 10)] + ['T', 'Q', 'K', 'A']
        c = Counter(self.cards)
        best = 0
        for extras in itertools.product(options, repeat=c['J']):
            c2 = Counter(c)
            if 'J' in c2:
                c2.pop('J')
            c2.update(extras)
            m = c2.most_common()
            if m[0][1] == 5:
                best = max(best, 6)
            if m[0][1] == 4:
                best = max(best, 5)
            if m[0][1] == 3 and m[1][1] == 2:
                best = max(best, 4)
            if m[0][1] == 3:
                best = max(best, 3)
            if m[0][1] == 2 and m[1][1] == 2:
                best = max(best, 2)
            if m[0][1] == 2:
                best = max(best, 1)
        return best
    
    @property
    def highcards(self):
        faces = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 1,
            'T': 10,
        }
        return tuple(int(faces.get(card, card)) for card in self.cards)


with open("7.txt") as f:
    lines = f.read().strip().splitlines()

hands: list[Hand] = []
for line in lines:
    cards, bid = line.split()
    hands.append(Hand(cards, int(bid)))

hands.sort(key=lambda hand: (hand.handtype, hand.highcards))
print(sum((i + 1) * hand.bid for i, hand in enumerate(hands)))
