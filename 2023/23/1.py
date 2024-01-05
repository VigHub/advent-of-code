from collections import defaultdict

with open('2023/23/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
m, n = len(lines), len(lines[0])
start, end = None, None
g = defaultdict(list)
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '#':
            continue
        if start is None:
            start = (i, j)
        end = (i, j)
        for d in [(0, 1, '>'), (1, 0, 'v'), (-1, 0, '^'), (0, -1, '<')]:
            x, y = i+d[0], j+d[1]
            if x < 0 or x >= m or y < 0 or y >= n:
                continue
            if lines[x][y] == '#':
                continue
            if c in '<>^v' and c != d[2]:
                continue
            g[i, j].append((i+d[0], j+d[1]))
imp_nodes = [node for node, nh in g.items() if len(nh) > 2]
imp_nodes.insert(0, start)
imp_nodes.append(end)
# print(start, end)
# print(imp_nodes)

gs = defaultdict(list)


def dfs(st, node, count=0):
    if node in imp_nodes and node != st:
        gs[st].append((node, count))
        return
    for nh in g[node]:
        if nh not in seen:
            seen.add(nh)
            dfs(st, nh, count+1)


for node in imp_nodes:
    seen = set([node])
    dfs(node, node)


# get path with longest dist from start to end
res = 0


def get_max_path_length(node, dist=0):
    global res
    if node == end:
        res = max(res, dist)
        return
    for nh, count in gs[node]:
        get_max_path_length(nh, dist+count)


get_max_path_length(start)
print(res)
