def convert_line(line):
    num = 0
    for c in line:
        num = num * 2 + (1 if c == '#' else 0)
    return num


def get_reflect(v):
    n = len(v)
    for i in range(n-1):
        for j in range(n):
            if i-j < 0 or i+j+1 >= n:
                return i+1
            if v[i-j] != v[i+j+1]:
                break
    return None


with open('2023/13/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
i_line = 0
grid = []
res = 0
n_lines = len(lines)
while i_line < n_lines:
    line = lines[i_line]
    if i_line == n_lines-1:
        grid.append(line)
    if line == '' or i_line == n_lines-1:
        rows = list(map(convert_line, grid))
        hl = get_reflect(rows)
        if not hl:
            cols = list(map(convert_line, zip(*grid)))
            vl = get_reflect(cols)
            print(f'{vl = }')
            res += vl
        else:
            print(f'{hl = }')
            res += hl*100
        grid = []
    else:
        grid.append(line)
    i_line += 1
print(res)
