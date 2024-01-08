with open('2015/5/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))


def part1():
    nices = 0
    for line in lines:
        vowels = 0
        for vowel in 'aeiou':
            vowels += line.count(vowel)
        if vowels < 3:
            continue
        double = False
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c + c in line:
                double = True
                break
        if not double:
            continue
        deny_words = ['ab', 'cd', 'pq', 'xy']
        deny = False
        for deny_word in deny_words:
            if deny_word in line:
                deny = True
                break
        if deny:
            continue
        nices += 1
    print(nices)


def part2():
    nices = 0
    for line in lines:
        pair = False
        for i in range(len(line) - 1):
            if line.count(line[i:i+2]) > 1:
                pair = True
                break
        if not pair:
            continue
        repeat = False
        for i in range(len(line) - 2):
            if line[i] == line[i+2]:
                repeat = True
                break
        if not repeat:
            continue
        nices += 1
    print(nices)


part1()
part2()
