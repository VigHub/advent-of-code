
with open('2023/4/in.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    n = len(lines)
    cards = [1] * n
    for i, line in enumerate(lines):
        _, numbers = line.split(':')
        win, extracted = numbers.split('|')
        win = set(win.strip().split(' '))
        extracted = extracted.strip().split(' ')
        count = 0
        for num in extracted:
            if num != "" and num in win:
                count += 1
        for j in range(count):
            if i+j+1 >= n:
                break
            cards[i+j+1] += cards[i]
print(cards)
print(sum(cards))
