def move_horizontally(c1, c2):
    if c1[1] > c2[1]:
        c2 = (c2[0], c2[1]+1)
    else:
        c2 = (c2[0], c2[1]-1)
    return c2

def move_vertically(c1, c2):
    if c1[0] > c2[0]:
        c2 = (c2[0]+1, c2[1])
    else:
        c2 = (c2[0]-1, c2[1])
    return c2


with open('2022/9/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    NUM_PARTS = 10
    snake = [(0,0) for _ in range(NUM_PARTS)]
    cells = set()
    cells.add((0,0))
    for line in lines:
        line = line.split(' ')
        move, steps = line[0], int(line[1])
        for step in range(steps):
            # move head
            if move == 'R':
                snake[0] = (snake[0][0], snake[0][1]+1)
            elif move == 'L':
                snake[0] = (snake[0][0], snake[0][1]-1)
            elif move == 'D':
                snake[0] = (snake[0][0]+1, snake[0][1])
            elif move == 'U':
                snake[0] = (snake[0][0]-1, snake[0][1])
            # move body
            for i in range(1, NUM_PARTS):
                part, part_before = snake[i], snake[i-1]
                if abs(part_before[0]-part[0]) <=1 and abs(part_before[1]-part[1]) <= 1:
                    # part near part_before, part remains in same position 
                    continue
                # move part
                if part_before[0] == part[0]:
                    # same column
                    part = move_horizontally(part_before, part)
                elif part_before[1] == part[1]:
                    # same row
                    part = move_vertically(part_before, part)
                else:
                    # diagonal
                    part = move_horizontally(part_before, part)
                    part = move_vertically(part_before, part)
                if i == NUM_PARTS-1:
                    # add position of tail
                    cells.add(part)
                snake[i] = part
            print(snake)
    print(cells)
    print(len(cells))

