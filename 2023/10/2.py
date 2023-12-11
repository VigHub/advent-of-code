from collections import deque

with open('2023/10/ex2.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    EMPTY_CHAR = 'o'
    VISITED_CHAR = ' '
    CYCLE_CHAR = 'X'
    grid = []
    for row in lines:
        row2 = ""
        for c in row:
            row2 += c+EMPTY_CHAR
        row2 = row2[:-1]
        grid.append(list(row2))
        grid.append(list(EMPTY_CHAR*len(row2)))
    grid = grid[:-1]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i%2==0 and j%2==1:
                if grid[i][j-1] in '-LF' or grid[i][j+1] in '-J7':
                    grid[i][j] = '-'
            elif i%2==1 and j%2==0:
                if grid[i-1][j] in '|F7' or grid[i+1][j] in '|LJ':
                    grid[i][j] = '|'
    

    m = len(grid)
    n = len(grid[0])
    def valid(i, j):
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
        for d in dirs.get(grid[i][j], [(0,0)]):
            x, y = i+d[0], j+d[1]
            if valid(x,y):
                grid[i][j] = CYCLE_CHAR
                return (x,y)
            
    
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
    grid[s[0]][s[1]] = CYCLE_CHAR
    while cell != end:
        new_cell = move_cycle(cell)
        # print(f'from {cell} to {new_cell}')
        cell = new_cell
    grid[end[0]][end[1]] = CYCLE_CHAR

    # visit out of cycle cell
    q = deque([])
    def flood(si, sj):
        if valid(si, sj):
            q.append((si,sj))
            while q:
                i, j = q.popleft()
                for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                    x, y = i+d[0], j+d[1]
                    if valid(x,y):
                        grid[x][y] = VISITED_CHAR
                        q.append((x,y))

    for row in grid:
        print(''.join(row).replace(EMPTY_CHAR, VISITED_CHAR))

    # first/last row
    for j in range(n):
        flood(0, j)
        flood(m-1, j)
    # first/last col
    for i in range(m):
        flood(i, 0)
        flood(i, n-1)
    
    print('-'*100)

    for row in grid:
        print(''.join(row))

    others = 0
    points = 0
    bar = 0
    hor = 0
    empty = 0
    for row in grid:
        for c in row:
            if c in '7FJL':
                others += 1
            if c == '.':
                points += 1
            if c == '-':
                hor += 1
            if c == '|':
                bar += 1
            if c == EMPTY_CHAR:
                empty += 1
    print(points, others, bar, hor, empty)
    print(sum([points, others, bar, hor, empty]))