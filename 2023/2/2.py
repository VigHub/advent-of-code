
def get_power(line: str):
    game_map = {'blue': 0, 'red': 0, 'green': 0}
    line = line.split(':')[1]
    matches = line.split(';')
    for match in matches:
        cubes = match.split(',')
        for cube in cubes:
            num, color = cube.strip().split(' ')
            num = int(num)
            game_map[color] = max(game_map[color], num)
    return game_map['blue'] * game_map['red'] * game_map['green']



res = 0
with open('./2/input.txt', 'r') as f:
    lines = f.readlines()
    for id, line in enumerate(lines, 1):
        res += get_power(line)
    
print(res)