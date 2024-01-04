import random

with open('2023/25/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
g = {}
for line in lines:
    node, nh = line.split(': ')
    if node not in g:
        g[node] = []
    for n in nh.split(' '):
        g[node].append(n)
        if n not in g:
            g[n] = []
        g[n].append(node)


# get shortest path from a to b
def get_path(g, a, b):
    visited = set()
    queue = [[a]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == b:
            return path
        if node not in visited:
            for adjacent in g[node]:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
            visited.add(node)


uses = {}
for _ in range(1000):  # higher range means more likely to be correct
    a, b = random.sample(list(g.keys()), 2)
    path = get_path(g, a, b)
    for i in range(len(path) - 1):
        edge = tuple(sorted([path[i], path[i + 1]]))
        uses[edge] = uses.get(edge, 0) + 1

# the three most used edges will be the three we need to cut
s_uses = sorted(uses.items(), key=lambda x: x[1], reverse=True)
banned = [p[0] for p in s_uses[:3]]
print(f'{banned = }')
num_nodes = len(g)
# remove edges from g
for edge in banned:
    g[edge[0]].remove(edge[1])
    g[edge[1]].remove(edge[0])


touched = set()


def dfs(g, start):
    touched.add(start)
    for node in g[start]:
        if node not in touched:
            dfs(g, node)


dfs(g, banned[0][0])
first_component = len(touched)
second_component = num_nodes - first_component
print(first_component*second_component)
