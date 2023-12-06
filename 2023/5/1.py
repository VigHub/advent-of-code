with open('2023/5/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    seeds = list(map(int, lines[0].split(':')[1].strip().split(' ')))
    i = 1
    n = len(lines)
    def convert(i, lines, seeds):
        seeds_copy = [s for s in seeds]
        while i<n and lines[i] != '':
            dest, source, how_much = list(map(int, lines[i].split(' ')))
            for j in range(len(seeds)):
                if source <= seeds_copy[j] < source+how_much:
                    seeds[j] = (seeds_copy[j] - source) + dest
                    print(f'Change from {seeds_copy[j]} to {seeds[j]} for range {source}~{source+how_much}->{dest}~{dest+how_much}') 
            i += 1
        print(seeds)
        print()
        return i+2

    i = 3
    print(seeds)
    print()
    while i < n:
        i = convert(i, lines, seeds)
    print(f'\nMin location is {min(seeds)}')