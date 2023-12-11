with open('2023/11/in.txt', 'r') as f:
    universe = list(map(lambda x: x.strip(), f.readlines()))
    GALAXY = '#'
    EXPANDED_TIMES = 1000000
    m = len(universe)
    n = len(universe[0])
    galaxy_rows = [0] * m
    galaxy_cols = [0] * n
    for i in range(m):
        for j in range(n):
            if universe[i][j] == GALAXY:
                galaxy_rows[i] += 1
                galaxy_cols[j] += 1

    added_rows = [0]*m
    added_cols = [0]*n
    for i in range(1, m):
        if galaxy_rows[i] == 0:
            added_rows[i] = added_rows[i-1]+1
        else:
            added_rows[i] = added_rows[i-1]
    for i in range(1, n):
        if galaxy_cols[i] == 0:
            added_cols[i] = added_cols[i-1]+1
        else:
            added_cols[i] = added_cols[i-1]

    # get galaxies
    galaxies = []
    for i in range(m):
        for j in range(n):
            if universe[i][j] == GALAXY:
                galaxies.append(
                    (i+added_rows[i]*(EXPANDED_TIMES-1), j+added_cols[j]*(EXPANDED_TIMES-1)))
    res = 0
    galaxies_len = len(galaxies)
    for i in range(galaxies_len):
        for j in range(i+1, galaxies_len):
            dist = abs(galaxies[i][0]-galaxies[j][0]) + \
                abs(galaxies[i][1]-galaxies[j][1])
            res += dist
    print(res)
