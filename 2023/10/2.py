from collections import deque

with open('2023/10/in.txt', 'r') as f:
    grid = list(map(lambda x: x.strip(), f.readlines()))
    grid = [list(row) for row in grid]
    EMPTY_CHAR = 'o'
    VISITED_CHAR = ' '
    CYCLE_CHAR = 'X'
    cycle_path = set()

    def increase(graph):
        increase_graph = []
        for row in graph:
            row2 = ""
            for c in row:
                row2 += c+EMPTY_CHAR
            row2 = row2[:-1]
            increase_graph.append(list(row2))
            increase_graph.append(list(EMPTY_CHAR*len(row2)))
        increase_graph = increase_graph[:-1]
        for i in range(len(increase_graph)):
            for j in range(len(increase_graph[i])):
                if i % 2 == 0 and j % 2 == 1:
                    if increase_graph[i][j-1] in '-LF' or increase_graph[i][j+1] in '-J7':
                        increase_graph[i][j] = '-'
                elif i % 2 == 1 and j % 2 == 0:
                    if increase_graph[i-1][j] in '|F7' or increase_graph[i+1][j] in '|LJ':
                        increase_graph[i][j] = '|'
        return increase_graph

    m = len(grid)
    n = len(grid[0])

    def valid1(i, j):
        return 0 <= i < m and 0 <= j < n and grid[i][j] not in f'{VISITED_CHAR}{CYCLE_CHAR}' and (i, j) not in cycle_path

    def valid2(i, j):
        return 0 <= i < m and 0 <= j < n and grid[i][j] not in f'{VISITED_CHAR}{CYCLE_CHAR}'

    def move_cycle(pos):
        dirs = {
            '|': [(1, 0), (-1, 0)],
            '-': [(0, 1), (0, -1)],
            'F': [(1, 0), (0, 1)],
            'L': [(0, 1), (-1, 0)],
            '7': [(0, -1), (1, 0)],
            'J': [(-1, 0), (0, -1)],
        }
        i, j = pos
        for d in dirs.get(grid[i][j], [(0, 0)]):
            x, y = i+d[0], j+d[1]
            if valid1(x, y):
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
    if valid1(s[0]-1, s[1]) and grid[s[0]-1][s[1]] in '|F7':
        endpoints.append((s[0]-1, s[1]))
    # down
    if valid1(s[0]+1, s[1]) and grid[s[0]+1][s[1]] in '|LJ':
        endpoints.append((s[0]+1, s[1]))
    # left
    if valid1(s[0], s[1]-1) and grid[s[0]][s[1]-1] in '-FL':
        endpoints.append((s[0], s[1]-1))
    # right
    if valid1(s[0], s[1]+1) and grid[s[0]][s[1]+1] in '-J7':
        endpoints.append((s[0], s[1]+1))
    assert len(endpoints) == 2
    start, end = endpoints
    cell = start
    cycle_path.add(s)
    cycle_path.add(start)
    while cell != end:
        new_cell = move_cycle(cell)
        # print(f'from {cell} to {new_cell}')
        cycle_path.add(new_cell)
        cell = new_cell
    cycle_path.add(end)

    for i in range(m):
        for j in range(n):
            if (i, j) not in cycle_path:
                grid[i][j] = '.'

    grid = increase(grid)
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] not in f'.{EMPTY_CHAR}':
                grid[i][j] = CYCLE_CHAR

    # visit out of cycle cell
    q = deque([])

    def flood(si, sj):
        q.append((si, sj))
        while q:
            i, j = q.popleft()
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i+d[0], j+d[1]
                if valid2(x, y):
                    # print(x, y, grid[x][y], '--')
                    grid[x][y] = VISITED_CHAR
                    q.append((x, y))

    for row in grid:
        print(''.join(row).replace(EMPTY_CHAR, VISITED_CHAR))
    # first/last row
    for j in range(n):
        if grid[0][j] != CYCLE_CHAR:
            flood(0, j)
        if grid[m-1][j] != CYCLE_CHAR:
            flood(m-1, j)
    # first/last col
    for i in range(m):
        if grid[i][0] != CYCLE_CHAR:
            flood(i, 0)
        if grid[i][n-1] != CYCLE_CHAR:
            flood(i, n-1)

    print('-'*100)

    for row in grid:
        print(''.join(row).replace(EMPTY_CHAR, VISITED_CHAR))

    points = 0
    for row in grid:
        for c in row:
            if c == '.':
                points += 1
    print(points)
