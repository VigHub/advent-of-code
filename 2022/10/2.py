def get_char(x, clock):
    if x-1 <= clock <= x+1:
        return '#'
    return '.'



with open('2022/10/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    special_clocks = set([20, 60, 100, 140, 180, 220])
    clock = 1
    x = 1
    res = 0
    row = "#"
    rows = []
    for line in lines:
        if clock == 0:
            rows.append(row)
            row = ""
        if line[0] == 'n':
            # noop takes 1 clock
            row += get_char(x, clock)
            clock = (clock + 1) % 40
        else:
            # addx takes 2 clocks
            addx = int(line.split()[1])
            row += get_char(x, clock)
            clock = (clock + 1) % 40
            if clock == 0:
                rows.append(row)
                row = ""
            x += addx
            row += get_char(x, clock)
            clock = (clock + 1) % 40
    if clock == 0:
        rows.append(row)
        row = ""
    print('\n'.join([' '.join(row) for row in rows]))
    
    