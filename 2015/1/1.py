with open('2015/1/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    for line in lines:
        res = 0
        for c in line:
            if c == '(':
                res += 1
            else:
                res -= 1
        print(res)
