from heapq import heappop, heappush


def get_elevation(c):
    if c == 'S':
        return 0
    if c == 'E':
        return 26
    return ord(c) - ord('a')


with open('2022/12/in.txt', 'r') as f:
    grid = [list(line.strip()) for line in f.readlines()]
m = len(grid)
n = len(grid[0])
start = None
end = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'E':
            end = (i, j)
    if start and end:
        break
dist = [[float('inf') for _ in range(n)] for _ in range(m)]
dist[end[0]][end[1]] = 0
heap = [(0, end)]
visited = set()
visited.add(end)
while heap:
    d, cell = heappop(heap)
    i, j = cell
    print(i, j, grid[i][j], dist[i][j])
    if grid[i][j] == 'a':
        print(d)
        break
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni = i + di
        nj = j + dj
        if not 0 <= ni < m or not 0 <= nj < n:
            continue
        if (ni, nj) in visited:
            continue
        if get_elevation(grid[i][j]) > get_elevation(grid[ni][nj]) + 1:
            continue
        if dist[ni][nj] < d + 1:
            continue
        dist[ni][nj] = d + 1
        visited.add((ni, nj))
        heappush(heap, (d + 1, (ni, nj)))
