from bisect import bisect_right


def exit_program(units):
    print(f'{rocks = }')
    print(f'{units-1 = }')
    exit()


rocks = set()
floor_row = 0

with open('2022/14/in.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))
    for line in lines:
        line = line.split(' -> ')
        for i in range(1, len(line)):
            col_pre, row_pre = list(map(int, line[i-1].split(',')))
            col, row = list(map(int, line[i].split(',')))
            floor_row = max(floor_row, row)
            if col_pre == col:
                for j in range(min(row_pre, row), max(row_pre, row)+1):
                    rocks.add((j, col))
            elif row_pre == row:
                for j in range(min(col_pre, col), max(col_pre, col)+1):
                    rocks.add((row, j))
    floor_row += 2
    print(f'{floor_row = }')
    units = 1
    while units < 10**12:
        col = 500
        row = 0
        if (row, col) in rocks:
            exit_program(units)
        while True:
            if row >= floor_row:
                exit_program(units)
            # try go down
            if (row+1, col) not in rocks:
                row += 1
                continue
            # try go left-down
            if (row+1, col-1) not in rocks:
                row += 1
                col -= 1
                continue
            # try go right-down
            if (row+1, col+1) not in rocks:
                row += 1
                col += 1
                continue
            # rest here
            break
        rocks.add((row, col))
        units += 1
        print(row, col)

exit_program(units)
