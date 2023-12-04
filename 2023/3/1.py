# diagonally
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
res = 0
with open('./3/in.txt', 'r') as f:
    lines = f.readlines()
    m, n = len(lines), len(lines[0])-1
    for i, line in enumerate(lines):
        j = 0
        while j<n:
            if line[j].isdigit():
                num = 0
                ok = False
                while j<n and line[j].isdigit():
                    num = num*10 + int(line[j])
                    if not ok:
                        for dir in dirs:
                            ii, jj = i+dir[0], j+dir[1]
                            if ii>=0 and ii<m and jj>=0 and jj<n and \
                                    not lines[ii][jj].isdigit() and lines[ii][jj] != '.':
                                ok = True
                                break
                    j += 1
                if ok:
                    res += num
                    print(num)
            else:
                j += 1
print(res)