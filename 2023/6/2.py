with open('2023/6/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    time = int(lines[0].split(':')[1].strip().replace(' ', ''))
    dist = int(lines[1].split(':')[1].strip().replace(' ', ''))
    print(f'Time is {time} seconds, distance is {dist} meters.')
    # find first time to press to do best
    l, r = 1, time
    while l < r:
        time_press_button = (l+r)//2
        time_for_race = time-time_press_button
        if time_press_button*time_for_race < dist:
            l = time_press_button+1
        else:
            r = time_press_button
    first_time = l
    # find last time to press to do best
    l, r = 1, time
    while l<r:
        time_press_button = (l+r)//2
        time_for_race = time-time_press_button
        if time_press_button*time_for_race >= dist:
            l = time_press_button+1
        else:
            r = time_press_button
    last_time = l-1
    print(f'Start is {first_time} seconds, end is {last_time} seconds.')
    print(f'Number of ways is {last_time-first_time+1}.')