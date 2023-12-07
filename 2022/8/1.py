with open('2022/8/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    grid = [[int(x) for x in line]for line in lines]
    m, n = len(grid), len(grid[0]) 
    visibles = set()
    # horizontal
    for i in range(m):
        maxi_lr = -1
        maxi_rl = -1
        for j in range(n):
            if grid[i][j] > maxi_lr:
                maxi_lr = grid[i][j]
                visibles.add((i, j))
            if grid[i][n-j-1] > maxi_rl:
                maxi_rl = grid[i][n-j-1]
                visibles.add((i, n-j-1))
    # vertical
    for j in range(n):
        maxi_ud = -1
        maxi_du = -1
        for i in range(m):
            if grid[i][j] > maxi_ud:
                maxi_ud = grid[i][j]
                visibles.add((i, j))
            if grid[m-i-1][j] > maxi_du:
                maxi_du = grid[m-i-1][j]
                visibles.add((m-i-1, j))
    print(len(visibles))