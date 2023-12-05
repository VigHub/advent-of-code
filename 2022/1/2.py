from heapq import heappop, heappush

def get_lines(file_name: str):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            yield line.strip()

heap = []

def add(val):
    heappush(heap, val)
    if len(heap) > 3:
        heappop(heap)

calories = 0
for i, line in enumerate(get_lines('2022/1/in.txt')):
    if line == '':
        add(calories)
        calories = 0
    else:
        calories += int(line)
if calories > 0:
    add(calories)
res = 0
while heap:
    res += heappop(heap)
print(res)