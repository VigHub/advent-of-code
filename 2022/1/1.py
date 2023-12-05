with open('2022/1/in.txt', 'r') as f:
    lines = f.readlines()
    max_calories = 0
    calories = 0
    for i, line in enumerate(lines):
        line = line.strip()
        if line == '' or i == len(lines) - 1:
            if calories > max_calories:
                max_calories = calories
            calories = 0
        else:
            calories += int(line)
    print(max_calories)