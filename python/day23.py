from collections import defaultdict
import neigh
with open('input') as f: lines = [x.strip('\n') for x in f]

elves = set()
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        if c == '#': elves.add((x,y))

def round(elves, n):
    prop = defaultdict(list)
    moved = False
    def do_prop(p,n):
        x,y = p
        propped = False
        if n%4 == 1: # North
            if all((q not in elves for q in [(x-1,y-1), (x,y-1), (x+1,y-1)])):
                prop[(x,y-1)].append(p)
                propped = True
        if n%4 == 2: # South
            if all((q not in elves for q in [(x-1,y+1), (x,y+1), (x+1,y+1)])):
                prop[(x,y+1)].append(p)
                propped = True
        if n%4 == 3: # West
            if all((q not in elves for q in [(x-1,y-1), (x-1,y), (x-1,y+1)])):
                prop[(x-1,y)].append(p)
                propped = True
        if n%4 == 0: # East
            if all((q not in elves for q in [(x+1,y-1), (x+1,y), (x+1,y+1)])):
                prop[(x+1,y)].append(p)
                propped = True
        return propped
    for p in elves:
        unhappy = any((q in elves for q in neigh.atrange(p,1)))
        if unhappy:
            do_prop(p,n) or do_prop(p,n+1) or do_prop(p,n+2) or do_prop(p,n+3)
    for p in prop:
        if len(prop[p]) == 1:
            elves.add(p)
            elves.remove(prop[p][0])
            moved = True
    return moved

for i in range(1,11): round(elves, i)
minx = min(x for x,y in elves)
maxx = max(x for x,y in elves)
miny = min(y for x,y in elves)
maxy = max(y for x,y in elves)
print((maxx+1 - minx) * (maxy+1 - miny) - len(elves))

i = 11
while round(elves, i): i += 1
print(i)
