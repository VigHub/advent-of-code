
import matplotlib.pyplot as plt
import networkx as nx

with open('2023/25/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
g = nx.Graph()
for line in lines:
    node, nh = line.split(': ')
    for n in nh.split(' '):
        g.add_edge(node, n)
nx.draw(g, with_labels=True, )
plt.show()
