with open('2022/5/in_changed.txt', 'r') as f:
    lines = list(map(lambda line: line.strip(), f.readlines()))
    n = len(lines)
    m = int(lines[0])
    stacks = [[] for _ in range(m)]
    for i in range(m):
        line = lines[i + 1]
        for c in line:
            stacks[i].append(c)
    i = m + 1
    while i < n:
        how_much, fr, to = list(map(int, lines[i].split('-')))
        for _ in range(how_much):
            stacks[to - 1].append(stacks[fr - 1].pop())
        i += 1
    res = ''
    for stack in stacks:
        res += stack.pop()
    print(res)
    
