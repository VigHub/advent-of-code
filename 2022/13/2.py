from functools import cmp_to_key


def convert(s, start):
    # print(s)
    res_list = []
    num = ''
    i = start
    while i < len(s):
        c = s[i]
        if c == '[':
            new_elem, ni = convert(s, i+1)
            i = ni
            res_list.append(new_elem)
        elif c in ',]':
            if num != '':
                res_list.append(int(num))
                num = ''
            if c == ']':
                return res_list, i
        else:
            num += c
        i += 1
    return res_list, len(s)


def right_order(l1, l2):
    l1_int = isinstance(l1, int)
    l2_int = isinstance(l2, int)
    if l1_int and l2_int:
        # both integer
        if l1 == l2:
            return 0
        return -1 if l1 < l2 else 1
    if not l1_int and not l2_int:
        # both list
        for i in range(min(len(l1), len(l2))):
            res = right_order(l1[i], l2[i])
            if res != 0:
                return res
        if len(l1) == len(l2):
            return 0
        return -1 if len(l1) < len(l2) else 1
    # one list, one int
    if l1_int:
        return right_order([l1], l2)
    return right_order(l1, [l2])


with open('2022/13/in.txt') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
res = 0
pair = 1
packets = []
for i in range(0, len(lines), 3):
    l1, _ = convert(lines[i], 1)
    l2, _ = convert(lines[i+1], 1)
    packets.append(l1)
    packets.append(l2)
packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(right_order))
first, second = None, None
for i, p in enumerate(packets, start=1):
    if p == [[2]]:
        first = i
    if p == [[6]]:
        second = i
    if first and second:
        break
print(f'{first = }, {second = }')
print(f'{first * second = }')
