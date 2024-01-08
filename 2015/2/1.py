with open('2015/2/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))


def part1():
    res = 0
    for line in lines:
        l, w, h = map(int, line.split('x'))
        res += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
    print(res)


def part2():
    res = 0
    for line in lines:
        l, w, h = map(int, line.split('x'))
        res += l * w * h + 2 * min(l + w, w + h, h + l)
    print(res)


part1()
part2()
