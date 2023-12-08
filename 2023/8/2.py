from math import gcd

with open('2023/8/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    instructions = lines[0]
    graph = {}
    nodes = []
    for line in lines[2:]:
        line = line.split(' = ')
        node = line[0]
        left, right = line[1][1:-1].split(', ')
        graph[node] = {'R': right, 'L': left}
        if node[-1] == 'A':
            # starting node
            nodes.append(node)

    nums = []
    for start in nodes:
        steps = 0
        not_arrived = True
        node = start
        while not_arrived:
            for instruction in instructions:
                node = graph[node][instruction]
                steps += 1
            if node[-1] == 'Z':
                not_arrived = False
                nums.append(steps)
    print(nums)
    def mcm(a, b):
        return a*b//gcd(a, b)
    res = 1
    for num in nums:
        res = mcm(res, num)
    print(res)
        