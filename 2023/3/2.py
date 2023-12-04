# diagonally
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
res = 0
gears = {}
with open('./3/in.txt', 'r') as f:
    lines = f.readlines()
    m, n = len(lines), len(lines[0])-1
    def ok(a,b):
        return a>=0 and a<m and b>=0 and b<n
    
    def add_gear(a, b, num):
        g = gears.get((a,b), [0, 1])
        gears[(a,b)] = [g[0]+1, g[1]*num]


    for i, line in enumerate(lines):
        j = 0
        while j<n:
            if line[j].isdigit():
                num = 0
                start_j = j
                while j<n and line[j].isdigit():
                    num = num*10 + int(line[j])
                    j += 1
                # check if num is near a gear
                # up
                for jj in range(start_j-1, j+1):
                    if ok(i-1, jj) and lines[i-1][jj] == '*':
                        add_gear(i-1, jj, num)
                # left
                if start_j > 0 and line[start_j-1] == '*':
                    add_gear(i, start_j-1, num)
                # right
                if j < n and line[j] == '*':
                    add_gear(i, j, num)
                # down
                for jj in range(start_j-1, j+1):
                    if ok(i+1, jj) and lines[i+1][jj] == '*':
                        add_gear(i+1, jj, num)
            else:
                j += 1

print(gears)
for g in gears.values():
    if g[0] == 2:
        res += g[1]
print(res)