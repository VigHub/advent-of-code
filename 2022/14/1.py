from bisect import bisect_right


def exit_program(units):
    # print(f'{rocks = }')
    print(f'{units-1 = }')
    exit()


rocks = {}
first_rocks = {}

with open('2022/14/in.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))
    mini = 100000
    maxi = 0
    for line in lines:
        line = line.split(' -> ')
        for i in range(1, len(line)):
            col_pre, row_pre = list(map(int, line[i-1].split(',')))
            col, row = list(map(int, line[i].split(',')))
            if col_pre == col:
                if col not in rocks:
                    rocks[col] = []
                for j in range(min(row_pre, row), max(row_pre, row)+1):
                    if j not in rocks[col]:
                        rocks[col].append(j)
            elif row_pre == row:
                for j in range(min(col_pre, col), max(col_pre, col)+1):
                    if j not in rocks:
                        rocks[j] = []
                    if row not in rocks[j]:
                        rocks[j].append(row)
    for rock in rocks.values():
        rock.sort()
    units = 1
    while units < 10**12:
        col = 500
        row = 0
        while True:
            if col not in rocks:
                exit_program(units)
            index_central = bisect_right(rocks[col], row)
            if index_central == len(rocks[col]):
                exit_program(units)
            i_row = rocks[col][index_central]-1
            # print(f'Possible row for central col {col} is {i_row = }')
            if col-1 not in rocks or i_row > rocks[col-1][-1]:
                exit_program(units)
            # try to go left
            index_left = bisect_right(rocks[col-1], i_row)
            i_row_pre = rocks[col-1][index_left]-1
            # print(f'Possible row for left col {col-1} is {i_row_pre = }')
            if i_row_pre != i_row:
                # go left
                assert i_row_pre > i_row
                col = col-1
                row = i_row_pre
                continue
            # try to go right
            if col+1 not in rocks:
                exit_program(units)
            index_right = bisect_right(rocks[col+1], i_row)
            i_row_post = rocks[col+1][index_right]-1
            # print(f'Possible row for right col {col+1} is {i_row_post = }')
            if i_row_post != i_row:
                # go right
                assert i_row_post > i_row
                col = col+1
                row = i_row_post
                continue
            # remain central
            rocks[col].insert(index_central, i_row)
            break
        units += 1
exit_program(units)
