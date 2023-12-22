from collections import defaultdict

with open('2023/22/in.txt', 'r') as f:
    lines = list(map(lambda x:  x.strip().split('~'), f.readlines()))
points = {}
blocks = []

for line in lines:
    start, end = line
    start = list(map(int, start.split(',')))
    end = list(map(int, end.split(',')))
    bl = []
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            for k in range(start[2], end[2]+1):
                points[i, j, k] = len(blocks)
                bl.append((i, j, k))
    blocks.append(bl)

blocks = sorted(blocks, key=lambda x: (x[0][2], x[0][0], x[0][0]))
# print(blocks)


def get_direction(s, e):
    if s[0] != e[0]:
        return [1, 0, 0], e[0]-s[0]
    elif s[1] != e[1]:
        return [0, 1, 0], e[1]-s[1]
    elif s[2] != e[2]:
        return [0, 0, 1], e[2]-s[2]


def move_block_part(b, d):
    return (b[0]+d[0], b[1]+d[1], b[2]+d[2])


def fall(blocks, points):
    fallen_blocks = [blocks[0]]
    for block in blocks:
        b_id = points[block[0]]
        stop = False
        while not stop:
            new_block = []
            for b in block:
                # move down block
                b = move_block_part(b, [0, 0, -1])
                if b[2] < 1 or (b in points and points[b] != b_id):
                    stop = True
                    break
                new_block.append(b)
            if not stop:
                for b in block:
                    del points[b]
                for b in new_block:
                    points[b] = b_id
                block = new_block
        fallen_blocks.append(block)
    return fallen_blocks


fallen_blocks = fall(blocks, points)

# get map of supporting blocks
supported_by = defaultdict(list)
for block in fallen_blocks:
    b_id = points[block[0]]
    for b in block:
        b = move_block_part(b, [0, 0, 1])
        if b in points and points[b] != b_id and b_id not in supported_by[points[b]]:
            supported_by[points[b]].append(b_id)


res = 0
for block in fallen_blocks:
    b_id = points[block[0]]
    disintegrated = True
    for b in block:
        b = move_block_part(b, [0, 0, 1])
        if b in points and points[b] != b_id and supported_by[points[b]] == [b_id]:
            disintegrated = False
            break
    if disintegrated:
        res += 1
        # print(f'Block {b_id} can be disintegrated')
# print(supported_by)
print(res)
