import re
import math
from copy import deepcopy
with open('input') as f:
    paras = [p.split('\n') for p in f.read().strip('\n').split('\n\n')]

def make_func(line):
    tok = line.strip().split(' ')
    if tok[4] == '+': op = lambda x,y: x+y
    if tok[4] == '*': op = lambda x,y: x*y
    if tok[5] == 'old':
        return lambda x: op(x, x)
    else:
        return lambda x: op(x, int(tok[5]))

monkeys = [] # list of [item_list, func, div_by, true_dest, false_dest, count]
for para in paras:
    monkey = []
    monkey.append(list(map(int, re.findall('[0-9]+', para[1]))))
    monkey.append(make_func(para[2]))
    monkey.append(int(para[3].split(' ')[-1]))
    monkey.append(int(para[4].split(' ')[-1]))
    monkey.append(int(para[5].split(' ')[-1]))
    monkey.append(0)
    monkeys.append(monkey)

lcm = math.lcm(*(m[2] for m in monkeys))

def monkey_business(monkeys, rounds, worry_div):
    for rnd in range(rounds):
        for m in monkeys:
            m[5] += len(m[0])
            while m[0]:
                item = m[0].pop()
                item = m[1](item)
                if worry_div:
                    item //= worry_div
                else:
                    item %= lcm
                if item % m[2] == 0:
                    monkeys[m[3]][0].append(item)
                else:
                    monkeys[m[4]][0].append(item)
    monkeys.sort(key = lambda m: -m[5])
    return monkeys[0][5] * monkeys[1][5]

print(monkey_business(deepcopy(monkeys), 20, 3))
print(monkey_business(deepcopy(monkeys), 10000, 0))
