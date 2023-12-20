with open('2023/19/in.txt') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
workflows = {}
parts = []
line_i = 0
while lines[line_i] != '':
    line = lines[line_i]
    name, wfs = line.split('{')
    wfs = wfs[:-1].split(',')
    workflows[name] = []
    for w in wfs:
        if '<' not in w and '>' not in w:
            workflows[name].append((-1, -1, -1, w))
            continue
        c = '<' if '<' in w else '>'
        prop = w.split(c)[0]
        num = int(w.split(':')[0][2:])
        nxt = w.split(':')[1]
        workflows[name].append((prop, c, num, nxt))
    line_i += 1
line_i += 1
for line in lines[line_i:]:
    line = line[1:-1].split(',')
    part = {}
    for l in line:
        prop, num = l.split('=')
        num = int(num)
        part[prop] = num
    parts.append(part)

res = 0
for part in parts:
    wname = 'in'
    ended = False
    while not ended:
        wf = workflows[wname]
        for w in wf:
            diff = (part.get(w[0], 1) - w[2]) * (-1 if w[1] == '<' else 1)
            if diff > 0 or w[0] == -1:
                if w[3] == 'A':
                    res += sum(part.values())
                    ended = True
                elif w[3] == 'R':
                    ended = True
                else:
                    wname = w[3]
                break
print(res)
