import ast
with open('input') as f: lines = [x.strip('\n') for x in f]
ssv = [x.split(' ') for x in lines]

values = {}
ops = {}
for line in ssv:
    monkey = line[0][:4]
    if line[1][0].isdigit():
        values[monkey] = int(line[1])
    else:
        ops[monkey] = [line[1], line[2], line[3]]
        values[monkey] = None

while values['root'] == None:
    for monkey in values:
        if values[monkey] == None:
            m1 = values[ops[monkey][0]]
            m2 = values[ops[monkey][2]]
            if m1 != None and m2 != None:
                op = ops[monkey][1]
                if op == '+': values[monkey] = m1 + m2
                if op == '-': values[monkey] = m1 - m2
                if op == '*': values[monkey] = m1 * m2
                if op == '/': values[monkey] = m1 / m2
print(int(values['root']))
