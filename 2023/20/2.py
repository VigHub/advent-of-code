from collections import deque

outbound = {}
module_type = {}
ffstate = {}
inbound = {}

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
button_pressed = 1
button_pressed_to = {}
bpt = 0

while bpt != (len(inbound)-1)*2:
    q = deque()
    # print('button -low-> broadcaster')
    for ob in outbound['broadcaster']:
        q.append((ob, 'broadcaster', L))
        # print(f'broadcaster -low-> {ob}')
    while q:
        outb, inb, pulse = q.popleft()
        if inb not in button_pressed_to:
            button_pressed_to[inb] = {}
        if pulse not in button_pressed_to[inb]:
            button_pressed_to[inb][pulse] = button_pressed
            bpt += 1
        if outb not in module_type:
            continue
        mtype = module_type[outb]
        if mtype == FF:
            if pulse == H:
                # flip flop received high, ignore
                continue
            # if receive low, change state and send state as pulse
            ffstate[outb] = 1-ffstate[outb]
            for nm in outbound[outb]:
                q.append((nm, outb, ffstate[outb]))
                # print(
                #     f'{outb} -{"high" if ffstate[outb] else "low"}-> {nm}')
        elif mtype == CON:
            inbound[outb][inb] = pulse
            con_pulse = 1-int(all(inbound[outb].values()))
            for nm in outbound[outb]:
                q.append((nm, outb, con_pulse))
                # print(
                #     f'{outb} -{"high" if con_pulse else "low"}-> {nm}')
        else:
            assert False
    button_pressed += 1


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


def LCM(a, b):
    return a*b//GCD(a, b)


inb_rx = list(inbound['rx'].keys())[0]
res = 1
mtype = module_type[inb_rx]
if mtype == CON:
    # wait until all inbound are high
    for i in inbound[inb_rx]:
        res = LCM(res, button_pressed_to[i][H])
print(res)
