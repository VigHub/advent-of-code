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
for line in lines:
    line = line.split(',')
    res = sum(map(HASH, line))
    print(res)
