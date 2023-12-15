with open('2015/1/ex.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    for line in lines:
        res = 0
        for i, c in enumerate(line, start=1):
            if c == '(':
                res += 1
            else:
                res -= 1
            if res == -1:
                print(i)
                break
