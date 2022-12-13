import ast
import functools
with open('input') as f:
    lines = [x.strip('\n') for x in f]
with open('input') as f:
    paras = [p.split('\n') for p in f.read().strip('\n').split('\n\n')]

def compare(a, b):
    if type(a) == int and type(b) == int:
        if a < b: return -1
        if a > b: return 1
        return 0
    if type(a) == int: a = [a]
    if type(b) == int: b = [b]
    if len(a) == 0 and len(b) == 0: return 0
    if len(a) == 0: return -1
    if len(b) == 0: return 1
    c = compare(a[0], b[0])
    if c != 0: return c
    return compare(a[1:],b[1:])

def valid(pair):
    return compare(ast.literal_eval(pair[0]), ast.literal_eval(pair[1])) == -1

print(sum(index for index,pair in enumerate(paras,start=1) if valid(pair)))

packets = [ast.literal_eval(line) for line in lines if line != '']
packets.append([[2]])
packets.append([[6]])
packets.sort(key=functools.cmp_to_key(compare))
print((packets.index([[2]])+1) * (packets.index([[6]])+1))
