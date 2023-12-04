res = 0
digits =['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
reverse_digits = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

def get_first_digit(word: str, rev=False):
    dig = reverse_digits if rev else digits
    i = 10**8
    d = 0
    for index, dig_word in enumerate(dig, start=1):
        f = word.find(dig_word)
        if f != -1 and f < i:
            i = f
            d = index
    for index, c in enumerate(word):
        if c.isdigit():
            if index < i: 
                d = ord(c)-ord('0')
                break
    return d



with open('./1/in.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        first = get_first_digit(line) 
        last = get_first_digit(line[::-1], rev=True)
        print(line, first, last)
        res += first*10 + last
print(res)