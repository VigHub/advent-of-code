with open('2023/8/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    instructions = lines[0]
    graph = {}
    for line in lines[2:]:
        line = line.split(' = ')
        node = line[0]
        left, right = line[1][1:-1].split(', ')
        graph[node] = {'R': right, 'L': left}
    steps = 0
    print(graph)
    # conditions for not having while True
    node = 'AAA'
    while steps < 10**12:
        for instruction in instructions:
            print(node, instruction, steps)
            if node == 'ZZZ':
                print(steps)
                exit()
            node = graph[node][instruction]
            steps += 1
    print('infinite loop')
        