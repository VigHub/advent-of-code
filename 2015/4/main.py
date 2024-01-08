import hashlib

secret_key = 'yzbqklnj'


def solve(zeros=5):
    for i in range(1000000000):
        str2hash = f'{secret_key}{i}'
        hashed = hashlib.md5(str2hash.encode()).hexdigest()
        if hashed.startswith('0' * zeros):
            print(i)
            break


solve()
solve(zeros=6)
