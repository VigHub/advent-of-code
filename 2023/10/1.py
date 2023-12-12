with open('2023/10/in.txt', 'r') as f:
    grid = list(map(lambda x: x.strip(), f.readlines()))
    m = len(grid)
    n = len(grid[0])

    def valid(i, j):
        return 0 <= i < m and 0 <= j < n

    def move(pos, pre):
        dirs = {
            '|': [(1, 0), (-1, 0)],
            '-': [(0, 1), (0, -1)],
            'F': [(1, 0), (0, 1)],
            'L': [(0, 1), (-1, 0)],
            '7': [(0, -1), (1, 0)],
            'J': [(-1, 0), (0, -1)],
        }
        i, j = pos
        for d in dirs[grid[i][j]]:
            x, y = i+d[0], j+d[1]
            if valid(x, y) and (x, y) != pre:
                print(f'Moving from {pos} ({grid[i][j]}) to {(x,y)}')
                return (x, y)

    s = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                s = (i, j)
                break
        if s:
            break
    # find first side of loop
    endpoints = []
    # up
    if valid(s[0]-1, s[1]) and grid[s[0]-1][s[1]] in '|F7':
        endpoints.append((s[0]-1, s[1]))
    # down
    if valid(s[0]+1, s[1]) and grid[s[0]+1][s[1]] in '|LJ':
        endpoints.append((s[0]+1, s[1]))
    # left
    if valid(s[0], s[1]-1) and grid[s[0]][s[1]-1] in '-FL':
        endpoints.append((s[0], s[1]-1))
    # right
    if valid(s[0], s[1]+1) and grid[s[0]][s[1]+1] in '-J7':
        endpoints.append((s[0], s[1]+1))
    assert len(endpoints) == 2
    start, end = endpoints
    cell = start
    pre = s
    # already count in cycle length S and final position
    cycle_length = 2
    while cell != end:
        new_cell = move(cell, pre)
        pre = cell
        cell = new_cell
        cycle_length += 1
    farthest_point = cycle_length // 2
    print(f'{farthest_point = }')
