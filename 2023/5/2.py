def merge(elems):
    elems = sorted(elems, key=lambda x: x[0])
    new_elems = [elems[0]]
    for elem in elems[1:]:
        if elem[0] <= new_elems[-1][1]+1:
            new_elems[-1][1] = max(elem[1], new_elems[-1][1])
        else:
            new_elems.append(elem)
    return new_elems


with open('2023/5/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    seeds_list = list(map(int, lines[0].split(':')[1].strip().split(' ')))
    ns = len(seeds_list)
    seeds = sorted([[seeds_list[i], seeds_list[i]+seeds_list[i+1]-1] for i in range(0, ns, 2)])
    i = 1
    n = len(lines)
    def convert(i, lines, seeds):
        seeds_copy = [s for s in seeds]
        seeds = []
        changes = []
        while i<n and lines[i] != '':
            dest, source, how_much = list(map(int, lines[i].split(' ')))
            changes.append([dest, source, how_much])
            i += 1

        for seed in seeds_copy:
            start = seed[0]
            end = seed[1]
            pre = []
            post = []
            interlap = False
            for change in changes:
                dest, source, how_much = change 
                print(f'{dest} {source}, {how_much} ---> {source}~{source+how_much-1}->{dest}~{dest+how_much-1}')
                start_change = source
                end_change = source+how_much-1
                if start > end_change or end < start_change:
                    continue
                diff = dest - source
                interlap = True
                print(f'-->Will change {[start, end]} for {[start_change, end_change]}, {diff = }:')
                if start < start_change:
                    pre.append([start, start_change-1])
                    print(f'Added pre seeds {[start, start_change-1]} for {change} ---> {source}~{source+how_much-1}->{dest}~{dest+how_much-1}')
                if end_change < end:
                    post.append([end_change+1, end])
                    print(f'Added post seeds {[end_change+1, end]} for {change} ---> {source}~{source+how_much-1}->{dest}~{dest+how_much-1}')
                new_seed = [max(start_change, start)+diff, min(end_change, end)+diff]
                seeds.append(new_seed)
                print(f'Interlap is {[max(start_change, start), min(end_change, end)]}, Added seeds {new_seed} for {change} ---> {source}~{source+how_much-1}->{dest}~{dest+how_much-1}')
            if not interlap:
                seeds.append(seed)
                print(f'No interlap, Added seeds {seed} for {change}')
                continue
            prepost = pre+post
            if len(prepost) == 0:
                continue
            merged = merge(prepost)[0]
            print(f'Merged {prepost} to {merged}, seed is {seed}')
            if merged != seed:
                for p in pre:
                    seeds.append(p)
                for p in post:
                    seeds.append(p) 
            else:
                print('Avoid adding pre post, merged is equal to seed')
        seeds = merge(seeds)
        return i+2, seeds

    i = 3
    j = 1
    while i < n:
        print('-'*170)
        print(f'Round {j} -> {seeds = }')
        i, seeds = convert(i, lines, seeds)
        print('-'*170)
        j += 1
    print(f'\nMin location is {min(min(seeds))} -> {seeds}')
    print(f'\nMin location is {min(min(seeds))}')