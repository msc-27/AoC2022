from collections import defaultdict
with open('input') as f: lines = [x.strip('\n') for x in f]
ssv = [x.split(' ') for x in lines]

def plot_line(p, q):
    px,py = p
    qx,qy = q
    if px == qx:
        direction = 1 if qy >= py else -1
        yield from ((px,y) for y in range(py, qy+direction, direction))
    else:
        direction = 1 if qx >= px else -1
        yield from ((x,py) for x in range(px, qx+direction, direction))

def string2point(s):
    x,y = map(int, s.split(','))
    return (x,y)

Map = defaultdict(lambda:' ')
for line in ssv:
    for p,q in (map(string2point,x) for x in zip(line[::2], line[2::2])):
        for r in plot_line(p,q): Map[r] = '#'

max_y = max(y for x,y in Map)
source = (500,0)

def drop_sand(with_baseline=False):
    p = source
    while True:
        x,y = p
        if y > max_y+1: return None
        if with_baseline and y == max_y+1:
            Map[p] = 'o'
            return p
        target = [q for q in [(x,y+1), (x-1,y+1), (x+1,y+1)] if Map[q] == ' ']
        if target:
            p = target[0]
            continue
        Map[p] = 'o'
        return p

units = 0
while drop_sand(): units += 1
print(units)
while True:
    units += 1
    if drop_sand(True) == source: break
print(units)
