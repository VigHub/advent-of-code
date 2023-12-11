with open('2023/11/in.txt', 'r') as f:
    universe = list(map(lambda x: x.strip(), f.readlines()))
    GALAXY = '#'
    galaxy_rows = [0] * len(universe)
    galaxy_cols = [0] * len(universe[0])
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == GALAXY:
                galaxy_rows[i] += 1
                galaxy_cols[j] += 1

    added_rows = sum([1 if r == 0 else 0 for r in galaxy_rows])
    added_cols = sum([1 if c == 0 else 0 for c in galaxy_cols])
    m = len(universe)+added_rows
    n = len(universe[0])+added_cols
    # expand universe
    expanded = []
    for i, gr in enumerate(galaxy_rows):
        universe_row = list(universe[i])
        count_col = 0
        for j, gc in enumerate(galaxy_cols):
            if gc == 0:
                universe_row.insert(j+count_col, '.')
                count_col += 1
        if gr == 0:
            expanded.append(list('.'*n))
        expanded.append(list(universe_row))

    # get galaxies
    galaxies = []
    for i in range(m):
        for j in range(n):
            if expanded[i][j] == GALAXY:
                galaxies.append((i, j))
    res = 0
    galaxies_len = len(galaxies)
    for i in range(galaxies_len):
        for j in range(i+1, galaxies_len):
            dist = abs(galaxies[i][0]-galaxies[j][0]) + \
                abs(galaxies[i][1]-galaxies[j][1])
            print(f'from {i+1} to {j+1}: {dist}')
            res += dist
    print(res)
