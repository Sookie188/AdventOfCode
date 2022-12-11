import re
import math

with open("AdventOfCode_2022/Day11/input.txt", "r") as fp:
    input = [line.rstrip() for line in fp.readlines()]

things = []
for i in range(0, len(input), 7):
    things.append(input[i:i+6])

splitted_things = []
for thing in things:
    splitted_thing = []
    for line in thing:
        splitted_thing.append(line.split())
    splitted_things.append(splitted_thing)


class Monkey:
    def __init__(self, id, items, operation, test, monkey_true, monkey_false):
        self.id = id
        self.items = items
        self.operator = operation[0]
        self.num = operation[1]
        self.test = test
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.thrown_items = 0

    def inspect(self):
        item = self.items[0]
        operator = self.operator
        if self.num == 'old':
            num = item
        else:
            num = int(self.num)
        if operator == '+':
            self.items[0] = item + num
            return self.items[0]
        if operator == '*':
            self.items[0] = item * num
            return self.items[0]

    def get_bored(self):
        self.items[0] = self.items[0] // 3
        return self.items[0]

    def do_black_magic_shit(self, lcm):
        self.items[0] %= lcm
        return self.items[0]

    def throw_to(self):
        if self.items[0] % int(self.test) == 0:
            return self.monkey_true
        else:
            return self.monkey_false

    def __str__(self):
        return 'Name: ' + self.id + ' Items: ' + str(self.items) + ' Thrown shit: ' + str(self.thrown_items)


def get_items(items_raw):
    items = []
    for i in range(2, len(items_raw)):
        items.append(int(re.findall(r'\d+', items_raw[i])[0]))
    return items


def get_operation(operation_raw):
    operation = []
    operation.extend([operation_raw[4], operation_raw[5]])
    return operation


def throw_item(monkey_from, monkey_to, monkeys):
    item = monkeys[monkey_from].items.pop(0)
    monkeys[monkey_to].items.append(item)
    monkeys[monkey_from].thrown_items += 1


def init_monkey(monkey_raw):
    monkid = monkey_raw[0][1][:-1]
    items = get_items(monkey_raw[1])
    operation = get_operation(monkey_raw[2])
    test = monkey_raw[3][3]
    monkey_true = monkey_raw[4][5]
    monkey_false = monkey_raw[5][5]
    return Monkey(monkid, items, operation, test, monkey_true, monkey_false)


def init_monkeys(input):
    monkeys = []
    for monkey_raw in input:
        monkeys.append(init_monkey(monkey_raw))
    return(monkeys)


def play_round(monkey, monkeys):
    while len(monkey.items) > 0:
        monkey.inspect()
        # print('inspected:', monkey.items[0], ' now: ', monkey.inspect())
        # monkey.get_bored()
        monkey.do_black_magic_shit(lcm)
        # print('bored division:', monkey.get_bored())
        # monkey.throw_to()
        # print('throw ', monkey.items[0], ' to monkey:', monkey.throw_to())
        throw_item(int(monkey.id),
                   int(monkey.throw_to()), monkeys)


monkeys = init_monkeys(splitted_things)

# I've stolen this from https://aoc.just2good.co.uk/2022/11
# Thank you for being smart af :)
lcm = math.lcm(*[int(monkey.test) for monkey in monkeys])
print('lcm:', lcm)

for _ in range(10000):
    # print(_)
    for monkey in monkeys:
        # print(monkey.items)
        play_round(monkey, monkeys)

result = [monkey.thrown_items for monkey in monkeys]
print(result)
result.sort(reverse=True)

monkey_business = result[0]*result[1]

print(monkey_business)
# print([str(monkey) for monkey in monkeys])
