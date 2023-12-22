from collections import defaultdict, deque
from time import perf_counter


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        print("Method " + method.__name__ + " took : " +
              "{:2.5f}".format(perf_counter() - t) + " sec")
        return ret

    return wrapper_method


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

blocks = sorted(blocks, key=lambda x: (x[0][2], x[0][0], x[0][1]))


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
    fallen_blocks = []
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
supports = defaultdict(list)
for block in fallen_blocks:
    b_id = points[block[0]]
    for b in block:
        b = move_block_part(b, [0, 0, 1])
        if b in points and points[b] != b_id:
            if b_id not in supported_by[points[b]]:
                supported_by[points[b]].append(b_id)
            if points[b] not in supports[b_id]:
                supports[b_id].append(points[b])


@profiler
def part1(fallen_blocks):
    res = 0
    for block in fallen_blocks:
        b_id = points[block[0]]
        disintegrated = True
        for supported in supports[b_id]:
            if len(supported_by[supported]) == 1:
                disintegrated = False
                break
        if disintegrated:
            res += 1
    print(res)


def bfs(b_id):
    q = deque([b_id])
    destroyed = 0
    spb = defaultdict(list)
    for k, v in supported_by.items():
        spb[k] = v.copy()
    first_b_id = b_id
    while q:
        for _ in range(len(q)):
            b_id = q.popleft()
            if len(spb[b_id]) == 0 or b_id == first_b_id:
                for supported in supports[b_id]:
                    spb[supported].remove(b_id)
                    if len(spb[supported]) == 0:
                        q.append(supported)
                        destroyed += 1
    return destroyed


@profiler
def part2(fallen_blocks):
    res = 0
    for block in fallen_blocks:
        b_id = points[block[0]]
        destroyable = False
        for supported in supports[b_id]:
            if len(supported_by[supported]) == 1:
                destroyable = True
                break
        if destroyable:
            destroyed = bfs(b_id)
            res += destroyed
            # print(f'Block {b_id} destroys { destroyed} blocks')
    print(res)


part1(fallen_blocks)
part2(fallen_blocks)
