with open('2023/9/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    res = 0
    for line in lines:
        nums = list(map(lambda x: int(x), line.split(' ')))
        print('-'*100)
        first = []
        not_finish = True
        while not_finish:
            not_finish = False
            print(nums)
            for n in nums:
                if n != 0:
                    not_finish = True
                    break
            new_nums = []
            for i in range(1, len(nums)):
                new_nums.append(nums[i] - nums[i - 1])
            first.append(nums[0])
            nums = new_nums
        num = 0
        for i in range(len(first)-2, -1, -1):
            num = first[i] - num
        print(num)
        res += num
    print('-'*100)
    print(f'{res = }')