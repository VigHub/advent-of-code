
res = 0
with open('2023/4/in.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        _, numbers = line.split(':')
        win, extracted = numbers.split('|')
        win = set(win.strip().split(' '))
        extracted = extracted.strip().split(' ')
        count = 0
        for num in extracted:
            if num != "" and num in win:
                count += 1
        if count == 0:
            continue
        res += (1 << (count - 1))
print(res)
