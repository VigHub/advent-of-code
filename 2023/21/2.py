from collections import deque

from tqdm import tqdm

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
N = len(lines)
points = []

for step in range(STEPS+2*N+1):
    new_q = deque()
    seen = set()
    while q:
        pos = q.popleft()
        for n in get_neighbours(pos):
            i, j = int(n.real), int(n.imag)
            i %= N
            j %= N
            nm = i+1j*j
            if nm in grid and grid[nm] == '.' and n not in seen:
                new_q.append(n)
                seen.add(n)
    q = new_q
    if step in [STEPS, STEPS+N, STEPS+2*N]:
        points.append((len(points), len(seen)))
        print(len(seen))


def get_second_grade(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    a = (x1*(y3-y2) + x2*(y1-y3) + x3*(y2-y1)) // ((x1-x2) * (x1-x3) * (x2-x3))
    b = (y2-y1)//(x2-x1) - a*(x1+x2)
    c = y1 - a*x1*x1 - b*x1
    return a, b, c


a, b, c = get_second_grade(points[0], points[1], points[2])
print(a, b, c)
x = 26501365 // 131
print(a*x*x + b*x + c)
