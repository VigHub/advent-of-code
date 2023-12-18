from heapq import heappush as push, heappop as pop

with open('2023/17/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
n = len(lines)
grid = {i+j*1j: int(lines[i][j]) for i in range(n) for j in range(n)}
visit = set()
# dist, counter (complex numbers have not order),  pos, where
heap = [(0, 0, 0, 1), (0, 0, 0, 1j)]
counter = 0
while heap:
    dist, _, pos, where = pop(heap)
    if pos == n-1+(n-1)*1j:
        print(dist)
        break
    if (pos, where) in visit:
        continue
    visit.add((pos, where))
    for d in 1j/where, -1j/where:
        for k in range(4, 10+1):
            new_pos = pos+d*k
            if new_pos in grid:
                counter += 1
                push(heap, (dist+sum(grid[pos+d*i]
                     for i in range(1, k+1)), counter, new_pos, d))
