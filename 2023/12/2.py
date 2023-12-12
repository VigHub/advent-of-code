from functools import cache


@cache
def dp(s: str, nums):
    s = s.lstrip('.')
    if s == '':
        return 1 if len(nums) == 0 else 0
    if len(nums) == 0:
        return 1 if s.count('#') == 0 else 0
    # start with #
    if s[0] == '#':
        first_group = nums[0]
        if len(s) < first_group or '.' in s[:first_group]:
            return 0
        if len(s) == first_group:
            return 1 if len(nums) == 1 else 0
        if s[first_group] == '#':
            return 0
        return dp(s[first_group+1:], nums[1:])
    # start with ?
    return dp('#'+s[1:], nums) + dp(s[1:], nums)


with open('2023/12/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    res = 0
    for t, line in enumerate(lines):
        row, nums = line.split(' ')
        nums += ','
        row = '?'.join([row for _ in range(5)])
        nums *= 5
        nums = nums[:-1]
        row += '.'
        nums = tuple(map(int, nums.split(',')))
        res_row = dp(row, nums)
        res += res_row
        print(f'Case #{t+1}: {res_row}')
    print(res)
