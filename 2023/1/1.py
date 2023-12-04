res = 0

def get_first_digit(word: str):
    for c in word:
        if c.isdigit():
            return ord(c)-ord('0')



with open('./1/in.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        res += 10*get_first_digit(line) + get_first_digit(line[::-1])

print(res)