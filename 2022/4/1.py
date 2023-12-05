with open('2022/4/in.txt', 'r') as f:
    lines = list(map(lambda line: line.strip(), f.readlines()))
    res = 0
    for line in lines:
        first, second = line.split(',')
        first = list(map(int, first.split('-')))
        second = list(map(int, second.split('-')))
        if first[0] <= second[0] and first[1] >= second[1]:
            res += 1
        elif first[0] >= second[0] and first[1] <= second[1]:
            res += 1
    print(res)
        