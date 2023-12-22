from collections import deque


def getsides(p1, p2):
    eq = 0
    for a1, a2 in zip(p1, p2):
        if a1 == a2:
            eq += 1
    if eq != 2:
        return 0
    for a1, a2 in zip(p1, p2):
        if a1 == a2:
            continue
        if min(a1, a2)+1 == max(a1, a2):
            return 1
    return 0


with open('2022/18/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
points = {tuple(map(int, l.split(','))) for l in lines}
n = len(points)
mini, maxi = [1000]*3, [-1000]*3


def get_surface(points):
    res = 0
    for p1 in points:
        sides = 6
        for j, a in enumerate(p1):
            mini[j] = min(mini[j], a)
            maxi[j] = max(maxi[j], a)
        for p2 in points:
            if p1 == p2:
                continue
            sides -= getsides(p1, p2)
        res += sides
    print(res)


get_surface(points)
print(mini, maxi)
MAX_LEN = 10000
outbounds = set()


def inside(p):
    for i, a in enumerate(p):
        if a < mini[i] or a > maxi[i]:
            return False
    return True


for i in range(mini[0]-1, maxi[0]+1):
    for j in range(mini[1]-1, maxi[1]+1):
        for k in range(mini[2]-1, maxi[2]+1):
            p = (i, j, k)
            if p in points or p in outbounds:
                continue
            seen = set()
            q = deque([p])
            seen.add(p)
            ok = True
            while q:
                p = q.popleft()
                for nh in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
                    np = list(p)
                    nh = list(nh)
                    for l in range(3):
                        np[l] += nh[l]
                    np = tuple(np)
                    if not inside(np):
                        ok = False
                        break
                    if np not in points and np not in outbounds and np not in seen:
                        q.append(np)
                        seen.add(np)
            if not ok:
                outbounds |= seen
                continue
            points |= seen
            # print(i, j, k)
            # print(seen)

get_surface(points)
