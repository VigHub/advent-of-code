
class Monkey:
    def __init__(self, monkey_id, items, operation: str, divisble_by, monkey_true, monkey_false):
        self.monkey_id = monkey_id
        self.items = items
        self.op = None
        self.second_number = None
        self.operation = operation
        self.get_operation()
        self.divisble_by = divisble_by
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.items_inspected = 0

    def get_operation(self):
        if '+' in self.operation:
            self.op = lambda x, y: x + y
        else:
            self.op = lambda x, y: x * y
        if self.operation.endswith('old'):
            self.second_number = 'old'
        else:
            self.second_number = int(self.operation[-2:])

    def operate(self, num):
        self.items_inspected += 1
        if self.second_number == 'old':
            return self.op(num, num)
        else:
            return self.op(num, self.second_number)

    def __repr__(self):
        return f'ID: {self.monkey_id}, items = {self.items}, items_inspected = {self.items_inspected}'


with open('2022/11/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
monkeys = {}
i = 0
while i < len(lines):
    monkey_id = int(lines[i][:-1].split(' ')[1])
    items = list(map(int, lines[i+1].split(':')
                 [1].replace(' ', '').split(',')))
    operation = lines[i+2].split(':')[1].strip()
    divisble_by = int(lines[i+3][-2:])
    monkey_true = int(lines[i+4][-2:])
    monkey_false = int(lines[i+5][-2:])
    monkeys[monkey_id] = Monkey(monkey_id, items, operation,
                                divisble_by, monkey_true, monkey_false)
    i += 7

ROUND = 1
while ROUND <= 20:
    for monkey_id, monkey in monkeys.items():
        # inspect elements
        while monkey.items:
            item = monkey.items.pop(0)
            # print(f'Monkey {monkey_id} inspects item {item}')
            # worry level change
            item = monkey.operate(item)
            # print(f'Worry level changed to {item}')
            # monkey gets bored
            item = int(item / 3)
            # print(f'Monkey gets bored, item becomes {item}')
            # monkey tests and throws item
            if item % monkey.divisble_by == 0:
                # print(f'Monkey {monkey_id} throws item to monkey {monkey.monkey_true}')
                monkeys[monkey.monkey_true].items.append(item)
            else:
                # print(f'Monkey {monkey_id} throws item to monkey {monkey.monkey_false}')
                monkeys[monkey.monkey_false].items.append(item)
    # print(f'After ROUND {ROUND}')
    # print('\n'.join([str(m) for m in monkeys.values()]))
    ROUND += 1
itmes_inspected = sorted([m.items_inspected for m in monkeys.values()])
res = itmes_inspected[-1]*itmes_inspected[-2]
print(res)
