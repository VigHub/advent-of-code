with open('2022/10/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    special_clocks = set([20, 60, 100, 140, 180, 220])
    clock = 1
    x = 1
    res = 0
    for line in lines:
        print(line, clock, x)
        if clock in special_clocks:
            print(clock, x)
            res += clock*x 
        if line[0] == 'n':
            # noop takes 1 clock
            clock += 1    
        else:
            addx = int(line.split()[1])
            clock += 1
            if clock in special_clocks:
                print(clock, x)
                res += clock*x
            x += addx
            clock += 1
    if clock in special_clocks:
        print(clock, x)
        res += clock*x 
    print(res)