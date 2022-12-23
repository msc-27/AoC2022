from collections import defaultdict
import re
import copy
with open('input') as f:
    paras = [p.split('\n') for p in f.read().strip('\n').split('\n\n')]
init_stacks = defaultdict(list)
for line in paras[0]:
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            init_stacks[(i-1)//4].insert(0, line[i])

def crane1(stacks, n, fr, to):
    for i in range(n):
        stacks[to].append(stacks[fr].pop())
def crane2(stacks, n, fr, to):
    stacks[to] += stacks[fr][-n:]
    stacks[fr][-n:] = []

stacks1 = copy.deepcopy(init_stacks)
stacks2 = copy.deepcopy(init_stacks)
for line in paras[1]:
    n, fr, to = list(map(int, re.findall('[0-9]+', line)))
    crane1(stacks1, n, fr-1, to-1)
    crane2(stacks2, n, fr-1, to-1)
print(''.join(stacks1[i].pop() for i in sorted(stacks1.keys())))
print(''.join(stacks2[i].pop() for i in sorted(stacks2.keys())))
