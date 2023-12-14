from bisect import bisect_right

with open('2023/14/in.txt', 'r') as f:
    rocks = [list(row)
             for row in list(map(lambda x: x.strip(), f.readlines()))]
m, n = len(rocks), len(rocks[0])
grid = [[] for _ in range(n)]
square_rocks = set()
for i in range(m):
    for j in range(n):
        if rocks[i][j] == '#':
            grid[j].append(i)
            square_rocks.add((i, j))
res = 0
for j in range(n):
    for i in range(m):
        if rocks[i][j] != 'O':
            continue
        index = bisect_right(grid[j], i)
        if index == 0:
            num = 0
        else:
            num = grid[j][index-1]+1
        grid[j].insert(index, num)
        res += m-num


def print_grid(grid):
    for i in range(m):
        for j in range(n):
            if (i, j) in square_rocks:
                print('#', end='')
            elif i in grid[j]:
                print('O', end='')
            else:
                print('.', end='')
        print()
    print()


print_grid(grid)
print(res)

'''
OOOO.#.O.. 10   
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1
'''
