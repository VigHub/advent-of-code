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


with open('in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
points = [list(map(int, l.split(','))) for l in lines]
n = len(points)
res = 0
for i in range(n):
    sides = 6
    p1 = points[i]
    for j in range(n):
        if i == j:
            continue
        p2 = points[j]
        sides -= getsides(p1, p2)
    res += sides
print(res)
