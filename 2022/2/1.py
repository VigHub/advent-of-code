with open('2022/2/in.txt', 'r') as f:
    lines = f.readlines()
    move = {'X': 1, 'Y': 2, 'Z': 3}
    result = {'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}
    res = 0
    for line in lines:
        a,b = line.strip().split()
        res += result[f'{a}{b}']+move[b]
    print(res)
