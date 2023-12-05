with open('2022/3/in.txt', 'r') as f:
    lines = map(lambda line: line.strip(), f.readlines())
    res = 0
    for line in lines:
        n = len(line)
        first = set(line[:n // 2])
        second = set(line[n // 2:])
        item = first.intersection(second).pop()
        if ord(item) > ord('Z'):
            priority = ord(item) - ord('a') + 1
        else:
            priority = ord(item) - ord('A') + 27
        res += priority
    print(res)
