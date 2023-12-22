from collections import deque

with open('2023/21/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
start = None
grid = {}
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == 'S':
            start = i+1j*j
            c = '.'
        grid[i+1j*j] = c


def get_neighbours(pos):
    dirs = [1, 1j, -1, -1j]
    for d in dirs:
        yield pos + d


q = deque()
q.append(start)
STEPS = 64

for _ in range(STEPS):
    new_q = deque()
    seen = set()
    while q:
        pos = q.popleft()
        for n in get_neighbours(pos):
            if n in grid and grid[n] == '.' and n not in seen:
                new_q.append(n)
                seen.add(n)
    q = new_q
print(len(seen))
