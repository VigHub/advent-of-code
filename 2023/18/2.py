with open('2023/18/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
G = []
pos = 0
G.append(pos)
moves = [1, 1j, -1, -1j]
mv = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
perimeter = 0
for line in lines:
    _, _, color = line.split()
    color = color[2:-1]
    n = int(color[:-1], 16)
    mid = int(color[-1])
    new_pos = pos+moves[mid]*n
    perimeter += abs(new_pos-pos)
    pos = new_pos
    G.append(pos)


def det(c1, c2):
    x1, y1 = c1.real, c1.imag
    x2, y2 = c2.real, c2.imag
    return x1*y2 - x2*y1


# shoelace formula
area = 0
n = len(G)
for i in range(0, n-1):
    c1, c2 = G[i], G[i+1]
    area += det(c1, c2)
area /= 2
# pick's theorem
# area = inside + perimeter/2 - 1
inside = area - perimeter/2 + 1
# result is inside + perimeter
print(int(inside+perimeter))
