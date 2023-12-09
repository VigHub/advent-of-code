def move_horizontally(h, t):
    if h[1] > t[1]:
        t = (t[0], t[1]+1)
    else:
        t = (t[0], t[1]-1)
    return t

def move_vertically(h, t):
    if h[0] > t[0]:
        t = (t[0]+1, t[1])
    else:
        t = (t[0]-1, t[1])
    return t


with open('2022/9/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    head = (0, 0)
    tail = (0, 0)
    cells = set()
    cells.add(head)
    for line in lines:
        line = line.split(' ')
        move, steps = line[0], int(line[1])
        for step in range(steps):
            if move == 'R':
                head = (head[0], head[1]+1)
            elif move == 'L':
                head = (head[0], head[1]-1)
            elif move == 'D':
                head = (head[0]+1, head[1])
            elif move == 'U':
                head = (head[0]-1, head[1])
            print(head, tail)
            if abs(head[0]-tail[0]) <=1 and abs(head[1]-tail[1]) <= 1:
                # tail near head, tail remains in same position 
                continue
            # move tail
            if head[0] == tail[0]:
                # same column
                tail = move_horizontally(head, tail)
            elif head[1] == tail[1]:
                # same row
                tail = move_vertically(head, tail)
            else:
                # diagonal
                tail = move_horizontally(head, tail)
                tail = move_vertically(head, tail)
            cells.add(tail)
    print(cells)
    print(len(cells))

'''
..##..
...##.
.####.
....#.
s###..
'''
