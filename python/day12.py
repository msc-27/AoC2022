from collections import defaultdict
import astar
import neigh
with open('input') as f:
    lines = [x.strip('\n') for x in f]
Map = defaultdict(lambda:'~')
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = c
def findin(d,x): return {v for v in d if d[v] == x}

# Search in reverse so that part 2 has a single starting point
start = findin(Map, 'E').pop()
end = findin(Map, 'S').pop()

def trans(p):
    valid = []
    elev_from = ord(Map[p]) if Map[p] != 'E' else ord('Z')
    for q in neigh.atmanhat(p, 1):
        elev_to = ord(Map[q]) if Map[q] != 'S' else ord('a')
        if elev_to - elev_from >= -1:
            valid.append((q, 1))
    return valid

print(astar.astar(start, trans).run(end)[0])
print(astar.astar(start, trans, lambda x: Map[x]=='a').run(None)[0])
