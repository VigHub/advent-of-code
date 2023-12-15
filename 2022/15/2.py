def get_nums(line):
    def get_num(l, nn):
        i = 0
        res = 0
        while l[nn-1] != '=':
            if line[nn-1] == '-':
                res *= -1
                nn -= 1
                break
            res += int(line[nn-1])*(10**i)
            i += 1
            nn -= 1
        return res, nn

    n = len(line)
    y, n = get_num(line, n)
    n -= 4
    x, _ = get_num(line, n)
    return x, y


file = '2022/15/in.txt'
with open(file, 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

res = 0
MIN = 0
MAX = 20 if 'ex' in file else 4000000
sensors = {}
beacons = set()
for line in lines:
    line = line.split(':')
    sensor = get_nums(line[0])
    beacon = get_nums(line[1])
    r = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    perimeter = set()
    for i in range(r+1):
        d = r+1-i
        perimeter.add((sensor[0]+d, sensor[1]+i))
        perimeter.add((sensor[0]-d, sensor[1]+i))
        perimeter.add((sensor[0]+d, sensor[1]-i))
        perimeter.add((sensor[0]-d, sensor[1]-i))

    sensors[sensor] = (perimeter, r)
    beacons.add(beacon)

possibles = set()
counter = 0
ns = len(sensors)
for s1, _ in sensors.items():
    for s2, _ in sensors.items():
        if s2 <= s1:
            continue
        s1_perimeter, _ = sensors[s1]
        s2_perimeter, _ = sensors[s2]
        intersection = s1_perimeter.intersection(s2_perimeter)
        new_intersection = []
        for its in intersection:
            if its in beacons or its in sensors or not MAX >= its[0] >= MIN or not MAX >= its[1] >= MIN:
                continue
            ok = True
            for s, p in sensors.items():
                r = p[1]
                if abs(s[0] - its[0]) + abs(s[1] - its[1]) <= r:
                    ok = False
                    break
            if ok:
                new_intersection.append(its)
        if len(new_intersection) == 1:
            possible = new_intersection.pop()
            if possible in possibles:
                print(f'Cell is {possible}')
                print(f'Tuning frequency: {possible[0]*4000000 + possible[1]}')
                exit()
            possibles.add(possible)
