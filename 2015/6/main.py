with open('2015/6/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))


def part1():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        line = line.split(' ')
        if line[0] == 'toggle':
            x1, y1 = map(int, line[1].split(','))
            x2, y2 = map(int, line[3].split(','))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] = 1 - grid[i][j]
        else:
            x1, y1 = map(int, line[2].split(','))
            x2, y2 = map(int, line[4].split(','))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] = 1 if line[1] == 'on' else 0
    print(sum(map(sum, grid)))


def part2():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        line = line.split(' ')
        if line[0] == 'toggle':
            x1, y1 = map(int, line[1].split(','))
            x2, y2 = map(int, line[3].split(','))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] += 2
        else:
            x1, y1 = map(int, line[2].split(','))
            x2, y2 = map(int, line[4].split(','))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] += 1 if line[1] == 'on' else -1
                    grid[i][j] = max(0, grid[i][j])
    print(sum(map(sum, grid)))


part1()
part2()
