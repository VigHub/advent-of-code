with open('2015/3/in.txt', 'r') as f:
    line = list(map(lambda x: x.strip(), f.readlines()))[0]


def part1():
    now = 0
    houses = set([now])
    dirs = {'^': 1j, 'v': -1j, '>': 1, '<': -1}
    for c in line:
        now += dirs[c]
        houses.add(now)
    print(len(houses))


def part2():
    now = [0, 0]
    houses = set([now[0]])
    dirs = {'^': 1j, 'v': -1j, '>': 1, '<': -1}
    for i, c in enumerate(line):
        now[i % 2] += dirs[c]
        houses.add(now[i % 2])
    print(len(houses))


part1()
part2()
