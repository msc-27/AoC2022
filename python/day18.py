import neigh
import astar
with open('input') as f: lines = [x.strip('\n') for x in f]
cubes = {tuple(map(int, line.split(','))) for line in lines}

covered = sum((x in cubes) for c in cubes for x in neigh.atmanhat(c,1))
print(6*len(cubes) - covered)

min_coord = min(min(x,y,z) for x,y,z in cubes)
max_coord = max(max(x,y,z) for x,y,z in cubes)
def in_range(p): return all(x in range(min_coord-1, max_coord+2) for x in p)

def trans(p): # neighbour function for flood fill
    for q in neigh.atmanhat(p,1):
        if in_range(q) and q not in cubes: yield (q,0)

start = (min_coord-1, min_coord-1, min_coord-1)
a = astar.astar(start, trans) # full search of state space
outside = {c for c,_ in a.run(None)}

# find the surface area of the flood fill (excluding bounding box)
touching = sum((x in outside or not in_range(x)) for c in outside for x in neigh.atmanhat(c,1))
print(6*len(outside) - touching)
