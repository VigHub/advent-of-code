with open('2022/6/in.txt', 'r') as f:
    lines = list(map(lambda line: line.strip(), f.readlines()))
    for line in lines:
        n = len(line)
        window = [line[0]]
        i = 1
        while i < n:
            while line[i] in window:
                window.pop(0)
            window.append(line[i])
            if len(window) == 4:
                print(window, i+1)
                break
            i += 1
        