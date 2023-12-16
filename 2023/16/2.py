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


def run(start_x, start_y, start_dir):
    energized = set()
    energized.add((start_x, start_y))
    visited = set()
    visited.add((start_x, start_y, start_dir))
    q = deque()
    q.append((start_x, start_y, start_dir))
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
    return len(energized)


res = 0
# top and down
for j in range(n):
    for d in dirs:
        res = max(res, run(0, j, d))
        res = max(res, run(n-1, j, d))
# left and right
for i in range(n):
    for d in dirs:
        res = max(res, run(i, 0, d))
        res = max(res, run(i, n-1, d))
print(res)
