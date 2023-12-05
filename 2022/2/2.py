with open('2022/2/in.txt', 'r') as f:
    lines = f.readlines()
    move = {'A': 1, 'B': 2, 'C': 3}
    result = {'X': 0, 'Y': 3, 'Z': 6}
    nx_move = {'X': {'A': 'C', 'B': 'A', 'C': 'B'}, 
               'Y': {'A': 'A', 'B': 'B', 'C': 'C'}, 
               'Z': {'A': 'B', 'B': 'C', 'C': 'A'}}
    res = 0
    for line in lines:
        a,b = line.strip().split()
        res += result[b]+move[nx_move[b][a]]
    print(res)
