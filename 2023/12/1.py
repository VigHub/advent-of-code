def test(row, nums):
    now = 0
    i = 0

    for j, c in enumerate(row):
        if c == '#':
            now += 1
        if c == '.' or j == len(row)-1:
            if now != 0:
                if i >= len(nums) or now != nums[i]:
                    return False
                i += 1
            now = 0
    return i == len(nums)


def next_combination(chars):
    for i in range(len(chars)-1, -1, -1):
        if chars[i] == '#':
            chars[i] = '.'
        else:
            chars[i] = '#'
            break
    return chars


with open('2023/12/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    res = 0
    for t, line in enumerate(lines):
        res_row = 0
        row, nums = line.split(' ')
        nums = list(map(int, nums.split(',')))
        chars_to_change = row.count('?')
        if chars_to_change == 0:
            print(f'Case #{t+1}: {res_row}')
            continue
        row = list(row)
        chars = ['.']*chars_to_change
        for i in range(2**chars_to_change):
            copy_row = row.copy()
            k = 0
            for j in range(len(row)):
                if row[j] == '?':
                    copy_row[j] = chars[k]
                    k += 1
            if test(copy_row, nums):
                res_row += 1
            chars = next_combination(chars)
        res += res_row
        print(f'Case #{t+1}: {res_row}')
    print(res)
