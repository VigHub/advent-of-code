from bisect import bisect_right

with open('2023/14/in.txt', 'r') as f:
    lines = [list(row)
             for row in list(map(lambda x: x.strip(), f.readlines()))]
m, n = len(lines), len(lines[0])


def tilt(rocks):
    grid = [[] for _ in range(n)]
    square_rocks = set()
    for i in range(m):
        for j in range(n):
            if rocks[i][j] == '#':
                grid[j].append(i)
                square_rocks.add((i, j))
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
    return grid, square_rocks


def get_grid(grid, square_rocks):
    new_grid = [['' for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if (i, j) in square_rocks:
                new_grid[i][j] = '#'
            elif i in grid[j]:
                new_grid[i][j] = 'O'
            else:
                new_grid[i][j] = '.'
    return new_grid


def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()


def get_string(grid):
    return ''.join([''.join(row) for row in grid])


def rotate_grid(grid):
    new_grid = [['' for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # rotate clock-wise
            new_grid[j][m-i-1] = grid[i][j]
    return new_grid


def get_res(grid):
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'O':
                res += m-i
    return res


grid = lines
TOT_CYCLE = int(1e9)
hash_map = {}
nodes_hash = []

for cycle in range(TOT_CYCLE):
    for _ in range(4):
        grid, square_rocks = tilt(grid)
        grid = get_grid(grid, square_rocks)
        # print('Tilt:')
        # print_grid(grid)
        grid = rotate_grid(grid)
        # print('Rotation:')
        # print_grid(grid)
    # print(f'After {cycle+1} cycles:')
    # print_grid(grid)
    hashed = get_string(grid)
    if hashed in hash_map:
        node = hash_map[hashed]
        cycle_length = cycle-node
        remaining_cycles = TOT_CYCLE-cycle-1
        mod = remaining_cycles % cycle_length
        print(f'Got cycle at {cycle}, with node {node}')
        print(f'Cycle length: {cycle_length}')
        print(f'Remaining cycles: {remaining_cycles}')
        print(f'mod: {mod}')
        print(nodes_hash)
        print(
            f'Res after {TOT_CYCLE} cycles: {nodes_hash[node+mod]}')
        break
    hash_map[hashed] = len(hash_map)
    nodes_hash.append(get_res(grid))
