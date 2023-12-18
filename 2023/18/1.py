from collections import deque

with open('2023/18/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
G = set()
now = 0
G.add(now)
minx, maxx, miny, maxy = 10**8, 0, 10**8, 0
moves = {'U': -1, 'L': -1j, 'D': 1, 'R': 1j}
for line in lines:
    d, n, color = line.split()
    n = int(n)
    color = color[1:-1]
    for _ in range(n):
        now += moves[d]
        G.add(now)
        minx = min(minx, now.real)
        maxx = max(maxx, now.real)
        miny = min(miny, now.imag)
        maxy = max(maxy, now.imag)
# find first point from which to start
cell = 0
for c in G:
    for m in moves.values():
        try_c = c + m
        if try_c not in G and miny <= try_c.imag <= maxy and minx <= try_c.real <= maxx:
            cell = try_c
            break

# expand
q = deque()
q.append(cell)
G.add(cell)
while q:
    c = q.popleft()
    for m in moves.values():
        try_c = c + m
        if try_c not in G and miny <= try_c.imag <= maxy and minx <= try_c.real <= maxx:
            q.append(try_c)
            G.add(try_c)
print(len(G))
