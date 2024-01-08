with open('2022/20/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
v = [f'{line}#{i}' for i, line in enumerate(lines)]
n = len(v)
v2 = [f'{line}#{i}' for i, line in enumerate(lines)]
# print([a[:-2] for a in v])
zero_val = None

for vn in v2:
    num = int(vn.split('#')[0])
    if num == 0:
        zero_val = vn
    index = v.index(vn)
    new_index = index+num+(-1 if num < 0 else 0)
    if new_index < 0:
        v.remove(vn)
        new_index = n+new_index
        v.insert(new_index, vn)
    elif new_index >= n:
        v.remove(vn)
        v.insert(new_index-n+1, vn)
    else:
        v.remove(vn)
        v.insert(new_index+(1 if num < 0 else 0), vn)

print([a[:-2] for a in v])
zero_index = v.index(zero_val)
res = 0
for i in [1000, 2000, 3000]:
    index = (zero_index+i) % n
    num = int(v[index].split('#')[0])
    print(num)
    res += num
print(res)
