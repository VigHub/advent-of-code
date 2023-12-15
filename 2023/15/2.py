def HASH(s: str):
    val = 0
    ascii_codes = list(map(ord, s))
    for a in ascii_codes:
        val += a
        val *= 17
        val %= 256
    return val


with open('2023/15/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
boxes = {i: {} for i in range(256)}
counter = [0] * 256

for line in lines:
    line = line.split(',')
    for l in line:
        if l[-1] == '-':
            label = l[:-1]
            box = HASH(label)
            if label in boxes[box]:
                del boxes[box][label]
        elif l[-2] == '=':
            label = l[:-2]
            box = HASH(label)
            focal_length = int(l[-1])
            if label in boxes[box]:
                p = boxes[box][label]
                boxes[box][label] = (p[0], focal_length)
            else:
                boxes[box][label] = (counter[box], focal_length)
                counter[box] += 1
        else:
            assert False

new_boxes = [None]*256
for i, box in boxes.items():
    new_boxes[i] = box

new_boxes = [sorted(box.values()) for box in new_boxes]
res = 0
print([(i, n) for i, n in enumerate(new_boxes) if len(n) > 0])
for i, box in enumerate(new_boxes, start=1):
    for j, b in enumerate(box, start=1):
        res += i*j*b[1]
print(res)
