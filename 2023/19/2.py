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


def dfs(wname, now):
    global res
    # print(wname, now, workflows.get(wname, "AR"))
    if wname in 'AR':
        if wname == 'A':
            print(now)
            res_now = 1
            for bounds in now.values():
                for bound in bounds:
                    res_now *= bound[1]-bound[0]+1
            res += res_now
        return
    wf = workflows[wname]
    for w in wf:
        if '<' not in w and '>' not in w:
            dfs(w[3], now)
        if '<' == w[1]:
            p = {n: v.copy() for n, v in now.items()}
            bounds_accepted = []
            bounds_refused = []
            for bound in p[w[0]]:
                if bound[0] < w[2] < bound[1]:
                    bounds_accepted.append([bound[0], w[2]-1])
                    bounds_refused.append([w[2], bound[1]])
                else:
                    bounds_accepted.append(bound)
                    bounds_refused.append(bound)
            p[w[0]] = bounds_accepted
            dfs(w[3], p)
            p[w[0]] = bounds_refused
            now = p
        if '>' == w[1]:
            p = {n: v.copy() for n, v in now.items()}
            bounds_accepted = []
            bounds_refused = []
            for bound in p[w[0]]:
                if bound[0] < w[2] < bound[1]:
                    bounds_accepted.append([w[2]+1, bound[1]])
                    bounds_refused.append([bound[0], w[2]])
                else:
                    bounds_accepted.append(bound)
                    bounds_refused.append(bound)
            p[w[0]] = bounds_accepted
            dfs(w[3], p)
            p[w[0]] = bounds_refused
            now = p


dfs('in', {p: [[1, 4000]] for p in 'xmas'})
# print()
# for w, f in workflows.items():
#    print(w, f)
print(res)
