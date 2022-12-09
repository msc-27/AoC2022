with open('input') as f: lines = [x.strip('\n') for x in f]
csv = [x.split(',') for x in lines]

def range2set(r):
    lo, hi = map(int,r.split('-'))
    return set(range(lo, hi+1))

ranges = [[range2set(x) for x in line] for line in csv]
print(sum(map(lambda x: x[0]<=x[1] or x[1]<=x[0], ranges)))
print(sum(map(lambda x: x[0] & x[1] != set(), ranges)))
