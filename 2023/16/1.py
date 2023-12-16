from collections import deque
with open('2023/16/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
go = {LEFT: (0, -1), RIGHT: (0, 1), UP: (-1, 0), DOWN: (1, 0)}
dirs = {
    LEFT: {
        '.': [LEFT],
        '-': [LEFT],
        '|': [DOWN, UP],
        '/': [DOWN],
        '\\': [UP],
    },
    RIGHT: {
        '.': [RIGHT],
        '-': [RIGHT],
        '|': [DOWN, UP],
        '/': [UP],
        '\\': [DOWN],
    },
    UP: {
        '.': [UP],
        '|': [UP],
        '-': [RIGHT, LEFT],
        '/': [RIGHT],
        '\\': [LEFT],
    },
    DOWN: {
        '.': [DOWN],
        '|': [DOWN],
        '-': [RIGHT, LEFT],
        '/': [LEFT],
        '\\': [RIGHT],
    },
}
n = len(lines)
def inside(i, j):
    return 0 <= i < n and 0 <= j < n

energized = set()
energized.add((0,0))
visited = set()
visited.add((0,0,RIGHT))
q = deque()
q.append((0,0,RIGHT))
while q:
    x, y, dir = q.popleft()
    c = lines[x][y]
    for d in dirs[dir][c]: 
        dx, dy = go[d]
        nx, ny = x + dx, y + dy
        if inside(nx, ny) and (nx, ny, d) not in visited:
            visited.add((nx, ny, d))
            energized.add((nx, ny))
            q.append((nx, ny, d))
print(len(energized))