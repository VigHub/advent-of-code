
def possible(line: str):
    possible_map = {'blue': 14, 'red': 12, 'green': 13}

    line = line.split(':')[1]
    matches = line.split(';')
    for match in matches:
        cubes = match.split(',')
        for cube in cubes:
            num, color = cube.strip().split(' ')
            num = int(num)
            if num > possible_map[color]:
                return False
    return True


res = 0
with open('./2/in.txt', 'r') as f:
    lines = f.readlines()
    for id, line in enumerate(lines, 1):
        if possible(line):
            res += id
print(res)