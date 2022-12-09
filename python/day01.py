with open('input') as f:
    paras = [p.split('\n') for p in f.read().strip('\n').split('\n\n')]

counts = sorted(sum(int(x) for x in p) for p in paras)

print(counts[-1])
print(sum(counts[-3:]))
