with open('2023/6/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    times = [int(t) for t in lines[0].split(':')[1].strip().split(' ') if t != '']
    dist = [int(d) for d in lines[1].split(':')[1].strip().split(' ') if d != '']
    res = 1
    for t, d in zip(times, dist):
        ways = 0
        for time_press_button in range(1, t):
            time_for_race = t-time_press_button
            dist_reached = time_press_button*time_for_race
            if dist_reached > d:
                ways += 1
                print(f'Pressing button at {time_press_button} seconds, will have {time_for_race} second and so {dist_reached} meters reached.')
        res *= ways
        print(f'There are {ways} ways for {t} seconds and {d} meters.')
    print(f'Product of ways is {res}')