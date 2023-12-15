

import re
from collections import defaultdict
from functools import cache
from itertools import product

flow_rate = {}
dist = defaultdict(lambda: 1000)
valves = set()
with open('2022/16/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    for line in lines:
        pattern = r'Valve ([A-Z]+) has flow rate=(\d+); valve* ([A-Z, ]+)'
        r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'
        # get values from regex
        print(re.findall(r, line))

        line = line.split(';')
        node = line[0][6:8]
        valves.add(node)
        i = line[0].find('=')
        f = int(line[0][i+1:])
        if f != 0:
            flow_rate[node] = f
        nodes = line[1].strip()[22:].split(',')
        for nd in nodes:
            dist[nd.strip(), node] = 1


# floyd-warshall algorithm to find distance between all nodes

for k, i, j in product(valves, valves, valves):
    dist[i, j] = min(dist[i, j], dist[i, k]+dist[k, j])


@cache
def dfs(time, u, vs, e):
    # return max([flow_rate[v]*(time-dist[u, v]-1) + dfs(time-dist[u, v]-1, v, vs-{v}, e)
    #             for v in vs if dist[u, v] < time] + [dfs(26, 'AA', vs, False) if e else 0])
    possibilities = [0]
    for v in vs:
        if dist[u, v] >= time:
            continue
        press = flow_rate[v]*(time-dist[u, v]-1) + \
            dfs(time-dist[u, v]-1, v, vs-{v}, e)
        possibilities.append(press)
    if e:
        possibilities.append(dfs(26, 'AA', vs, False))
    return max(possibilities)


print(dfs(26, 'AA', frozenset(flow_rate), True))
