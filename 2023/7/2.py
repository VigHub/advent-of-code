from collections import defaultdict

# joker is now the weakest
poker_cards = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13}


def get_type(hand: str):
    counter = defaultdict(int)
    for c in hand:
        counter[c] += 1
    five, four, three, two = 0, 0, 0, 0
    jokers = 0
    for k, v in counter.items():
        if k == 'J':
            jokers = v
        elif v == 5:
            five = 1
        elif v == 4:
            four = 1
        elif v == 3:
            three = 1
        elif v == 2:
            two += 1
    # print(counter, jokers)
    if five or (four and jokers == 1) or (three and jokers == 2) or (two and jokers == 3) or (jokers >= 4):
        return 7
    if four or (three and jokers == 1) or (two == 1 and jokers == 2) or (jokers == 3):
        return 6
    # (two == 1 and jokers == 2) -> this is not considered as it's best to create four in this case
    if (three and two == 1) or (two == 2 and jokers == 1):
        return 5
    if three or (two and jokers == 1) or (jokers == 2):
        return 4
    # (two == 1 and jokers == 1) -> this is not considered as it's best to create three in this case
    if two == 2:
        return 3
    if two == 1 or jokers == 1:
        return 2
    return 1


# print('5AJ3J', get_type('5AJ3J'))


def get_order(hand: str):
    p = [poker_cards[h] for h in hand]
    return [get_type(hand), p]


with open('2023/7/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    hands_with_bits = [line.split() for line in lines]
    hands_sorted = sorted(hands_with_bits, key=lambda x: get_order(x[0]))
    # print(hands_sorted)
    for hand in hands_sorted:
        print(hand)
    res = 0
    for i, hand in enumerate(hands_sorted, start=1):
        res += i*int(hand[1])
    print(res)
