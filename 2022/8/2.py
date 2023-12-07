with open('2022/8/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    grid = [[int(x) for x in line]for line in lines]
    m, n = len(grid), len(grid[0]) 
    up = [0 for _ in range(10)]
    down = [0 for _ in range(10)]
    score_l = [[0 for _ in range(n)] for _ in range(m)]
    score_r = [[0 for _ in range(n)] for _ in range(m)]
    score_u = [[0 for _ in range(n)] for _ in range(m)]
    score_d = [[0 for _ in range(n)] for _ in range(m)]

    def get_view(tree, counter, pos, start=0, mini=False, ):
        if mini:
            score = start
            for i in range(9, tree-1, -1):
                score = min(score, counter[i])
        else:
            score = start
            for i in range(tree, 10):
                score = max(score, counter[i])
        return abs(score - pos)

    # horizontal
    for i in range(m):
        left = [0 for _ in range(10)]
        right = [n-1 for _ in range(10)] 
        for j in range(1, n):
            l = grid[i][j]
            r = grid[i][n-j-1]
            score_l[i][j] = get_view(l, left, j)
            left[l] = j
            score_r[i][n-j-1] = get_view(r, right, n-j-1, n-1, True)
            right[r] = n-j-1
      
                
    # vertical
    for j in range(n):
        up = [0 for _ in range(10)]
        down = [m-1 for _ in range(10)]
        for i in range(1, m):
            u = grid[i][j]
            d = grid[m-i-1][j]
            score_u[i][j] = get_view(u, up, i)
            up[u] = i
            score_d[m-i-1][j] = get_view(d, down, m-i-1, m-1, True)
            down[d] = m-i-1
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, score_u[i][j]*score_d[i][j]*score_l[i][j]*score_r[i][j])

    def print_grid(grid):
        for row in grid:
            print(row)

    print('\nscore_l:')
    print_grid(score_l)
    print('\nscore_r:')
    print_grid(score_r)
    print('\nscore_u:')
    print_grid(score_u)
    print('\nscore_d:')
    print_grid(score_d)

    print(f'{res = }')