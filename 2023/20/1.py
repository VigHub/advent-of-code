from collections import deque

outbound = {}
module_type = {}
ffstate = {}
inbound = {}

MAX_ROUNDS = 1000
FF, CON = '%', '&'
L, H = 0, 1
OFF, ON = 0, 1

with open('2023/20/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
for line in lines:
    name, nxt = line.split(' -> ')
    nxt = nxt.split(', ')
    c = ''
    if name != 'broadcaster':
        c = name[0]
        name = name[1:]
    module_type[name] = c
    if c == FF:
        ffstate[name] = OFF
    if name not in outbound:
        outbound[name] = []
    for n in nxt:
        outbound[name].append(n)
        if n not in inbound:
            inbound[n] = {}
        inbound[n][name] = L
r = 1
high_pulses = 0
low_pulses = 0

while r <= MAX_ROUNDS:
    q = deque()
    low_pulses += 1
    # print('button -low-> broadcaster')
    for ob in outbound['broadcaster']:
        q.append((ob, 'broadcaster', L))
        # print(f'broadcaster -low-> {ob}')
        low_pulses += 1
    while q:
        outb, inb, pulse = q.popleft()
        if outb not in module_type:
            if pulse == L:
                print(f'arrived {pulse} to {outb}')
            continue
        mtype = module_type[outb]
        if mtype == FF:
            if pulse == H:
                # flip flop received high, ignore
                # print(f'{outb} ignore high pulse from {inb}')
                continue
            # if receive low, change state and send state as pulse
            ffstate[outb] = 1-ffstate[outb]
            for nm in outbound[outb]:
                q.append((nm, outb, ffstate[outb]))
                # print(
                #     f'{outb} -{"high" if ffstate[outb] else "low"}-> {nm}')
                if ffstate[outb] == H:
                    high_pulses += 1
                else:
                    low_pulses += 1
        elif mtype == CON:
            inbound[outb][inb] = pulse
            con_pulse = 1-int(all(inbound[outb].values()))
            for nm in outbound[outb]:
                q.append((nm, outb, con_pulse))
                # print(
                #     f'{outb} -{"high" if con_pulse else "low"}-> {nm}')
                if con_pulse == H:
                    high_pulses += 1
                else:
                    low_pulses += 1
        else:
            assert False
    r += 1
print(high_pulses, low_pulses)
print(high_pulses*low_pulses)
