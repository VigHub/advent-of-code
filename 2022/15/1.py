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


file = '2022/15/ex.txt'
with open(file, 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

res = 0
ROW = 10 if 'ex' in file else 2000000
sensors = []
beacons = []
possibles = set()
for line in lines:
    line = line.split(':')
    sensor = get_nums(line[0])
    beacon = get_nums(line[1])
    sensors.append(sensor)
    beacons.append(beacon)
for sensor, beacon in zip(sensors, beacons):
    dist = abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])
    row_dist = abs(ROW-sensor[1])
    secure = dist-row_dist
    if secure < 0:
        print(sensor, beacon, secure, 0)
        continue
    print(sensor, beacon, secure, secure*2+1)
    possibles.add(sensor[0])
    for i in range(secure):
        possibles.add(sensor[0]+i+1)
        possibles.add(sensor[0]-i-1)
for beacon in beacons:
    if beacon[1] == ROW and beacon[0] in possibles:
        possibles.remove(beacon[0])
# print(possibles)
print(len(possibles))
