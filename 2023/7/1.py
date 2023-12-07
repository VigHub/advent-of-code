from collections import defaultdict

poker_cards = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}


def get_type(hand: str):
    counter = defaultdict(int)
    for c in hand:
        counter[c] += 1
    five, four, three, two = 0, 0, 0, 0
    for v in counter.values():
        if v == 5:
            five = 1
        elif v == 4:
            four = 1
        elif v == 3:
            three = 1
        elif v == 2:
            two += 1
    if five:
        return 7
    if four:
        return 6
    if three and two:
        return 5
    if three:
        return 4
    if two == 2:
        return 3
    if two == 1:
        return 2
    return 1


def get_order(hand: str):
    p = [poker_cards[h] for h in hand]
    return [get_type(hand), p]


with open('2023/7/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    hands_with_bits = [line.split() for line in lines]
    hands_sorted = sorted(hands_with_bits, key=lambda x: get_order(x[0]))
    print(hands_sorted)
    res = 0
    for i, hand in enumerate(hands_sorted, start=1):
        res += i*int(hand[1])
    print(res)
