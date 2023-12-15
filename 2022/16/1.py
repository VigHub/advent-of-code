
from functools import cache

graph = {}
flow_rate = {}
node_id = {}
with open('2022/16/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    for line in lines:
        line = line.split(';')
        node = line[0][6:8]
        if node not in graph:
            graph[node] = []
        node_id[node] = len(node_id)
        i = line[0].find('=')
        flow_rate[node] = int(line[0][i+1:])
        nodes = line[1].strip()[22:].split(',')
        for nd in nodes:
            graph[node].append(nd.strip())

MAX_TIME = 30
print(graph)
ALL_OPEN = 0
for node, fr in flow_rate.items():
    if fr != 0:
        ALL_OPEN |= (1 << node_id[node])


@cache
def dfs(time: int, node: str, opens: int):
    if time > MAX_TIME or opens == ALL_OPEN:
        return 0
    open_and_move = 0
    only_move = 0
    if flow_rate[node] != 0 and (((1 << node_id[node]) & opens) == 0):
        # open node
        opens |= (1 << node_id[node])
        added = (MAX_TIME-time)*flow_rate[node]
        nh_added = 0
        for nd in graph[node]:
            # move to others nodes
            nh_added = max(nh_added, dfs(time+2, nd, opens))
        res = added+nh_added
        # print(time, node, bin(opens)[2:], res)
        open_and_move = res
    # move to others nodes
    nh_added = 0
    for nd in graph[node]:
        nh_added = max(nh_added, dfs(time+1, nd, opens))
    res = nh_added
    # print(time, node, bin(opens)[2:], res)
    only_move = res
    return max(open_and_move, only_move)


print(dfs(1, 'AA', 0))
