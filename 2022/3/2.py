with open('2022/3/in.txt', 'r') as f:
    lines = list(map(lambda line: line.strip(), f.readlines()))
    n = len(lines)
    res = 0
    for i in range(0, n, 3):
        first = set(lines[i])
        second = set(lines[i+1])
        third = set(lines[i+2])
        item = first.intersection(second).intersection(third).pop()
        if ord(item) > ord('Z'):
            priority = ord(item) - ord('a') + 1
        else:
            priority = ord(item) - ord('A') + 27
        res += priority
    print(res)
